import os
from typing import Any, Literal

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from redis import Redis  # type: ignore
from rq import Queue

from database import SessionLocal, Base, engine
import auth, models, schemas, service


app: FastAPI = FastAPI()
q: Queue = Queue(connection=Redis())
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
Base.metadata.create_all(bind=engine)  # type: ignore
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
) -> models.User:
    token_data = auth.verify_access_token(token)

    user = (
        service.get_user_by_email(db, email=token_data.email)
        if token_data.email is not None
        else None
    )

    if user is None:
        raise auth.CredentialsException

    return user


@app.get("/")
async def root() -> str:
    return "Pong"


@app.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> dict[str, str]:
    user: models.User | Literal[False] = service.authenticate_user(
        form_data.username, form_data.password, db
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth.create_access_token(data={"sub": str(user.email)})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user: models.User | None = service.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return service.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    _: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    users = service.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(
    user_id: int,
    _: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db_user = service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/jobs/", response_model=list[schemas.Job])
def read_jobs(
    skip: int = 0,
    limit: int = 100,
    user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    x = lambda job: {**job.__dict__, "url": job.get_url()}

    jobs = service.get_jobs(db=db, owner_id=user.id, skip=skip, limit=limit)  # type: ignore
    jobs_with_url = [x(job) for job in jobs]

    return jobs_with_url


@app.get("/jobs/{job_id}/download", response_class=FileResponse)
async def send_job_file(job_id):
    return f"{DIR_PATH}/completed_jobs/{job_id}.csv"


@app.post("/jobs/", response_model=schemas.Job)
def create_job(
    job: schemas.JobCreate,
    user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db_job = service.create_job(db=db, job=job, user=user)
    started_job = service.start_fetch(db, q, db_job)
    return started_job
