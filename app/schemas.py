from datetime import datetime
from pydantic import BaseModel
from models import Status


class JobBase(BaseModel):
    contract_address: str
    from_block: int
    to_block: int
    name: str


class JobCreate(JobBase):
    pass


class Job(JobBase):
    id: int
    creation_date: datetime
    status: Status
    url: str | None = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    jobs: list[Job] = []

    class Config:
        orm_mode = True
