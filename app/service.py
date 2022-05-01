from typing import Literal, Optional
from sqlalchemy.orm import Session
from rq import Queue

from database import SessionLocal
from auth import get_password_hash, verify_password
import models, schemas, fetch
import mailer


def authenticate_user(
    email: str, password: str, db: Session
) -> models.User | Literal[False]:
    user = get_user_by_email(db, email)
    if not user:
        return False
    if user.hashed_password is None:
        return False
    if not verify_password(password, str(user.hashed_password)):
        return False
    return user


def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_jobs(
    db: Session, owner_id: int, skip: int = 0, limit: int = 100
) -> list[models.Job]:
    return (
        db.query(models.Job)
        .filter(models.Job.owner_id == owner_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_job(db: Session, job: schemas.JobCreate, user: models.User) -> models.Job:
    db_job = models.Job(
        contract_address=job.contract_address,
        name=job.name,
        status=models.Status.PENDING,
        owner=user,
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def update_job(job_id: int, status: models.Status) -> None:
    session = SessionLocal()
    job = session.query(models.Job).filter(models.Job.id == job_id).one()

    job.status = status
    session.add(job)
    session.commit()
    session.refresh(job)
    session.close()


def notify_job(job_id: int) -> None:
    session = SessionLocal()
    job: models.Job = session.query(models.Job).filter(models.Job.id == job_id).one()
    owner: models.User = job.owner

    mailer.notify(str(owner.email), job)
    session.close()


def start_fetch(db: Session, q: Queue, job: models.Job):
    process = q.enqueue(
        fetch.fetch,
        job_timeout="2h",
        args=(
            str(job.id),
            job.contract_address,
        ),
    )
    update = q.enqueue(
        update_job,
        job_timeout="2h",
        args=(job.id, models.Status.SUCCESS),
        depends_on=process,
    )
    q.enqueue(notify_job, job_timeout="2h", args=(job.id,), depends_on=update)

    job.status = models.Status.RUNNING  # type: ignore
    db.add(job)
    db.commit()
    db.refresh(job)

    return job
