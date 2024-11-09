import datetime

from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str
    content: str
    posted_date: datetime.date


class PostCreate(PostBase):
    user_id: int = Field(gt=0)


class PostSchema(PostCreate):
    id: int

    class Config:
        orm_mode = True
