import hashlib

from typing import Any
from enum import Enum

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    DateTime,
    Integer,
    String,
    Enum as DBEnum,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Status(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class User(Base):  # type: ignore
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    jobs: Any = relationship("Job", back_populates="owner")


class Job(Base):  # type: ignore
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    contract_address = Column(String, index=True)
    from_block = Column(Integer)
    to_block = Column(Integer)
    name = Column(String, index=True)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(DBEnum(Status))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner: Any = relationship("User", back_populates="jobs")

    def get_hash(self):
        return hashlib.md5(str(self.id).encode()).hexdigest()

    def get_url(self):
        return f"localhost:8000/jobs/{self.get_hash()}/download"
