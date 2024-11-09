# Has pydantic models
from pydantic import EmailStr, BaseModel, validator, PydanticValueError, Field


# base user class that contains fields that will be used in both reading and creation of user
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str


# create user model that includes base fields plus fields needed only at time of creation of user
class UserCreate(UserBase):
    password: str

    @validator("password")
    def password_alphanumeric(cls, value):
        if not value.isalnum():
            raise ValueError("Password must be alphanumeric")
        return value

    @validator("password")
    def password_length(cls, value):
        if len(value) > 8:
            raise ValueError("Password length should not exceed 8 characters")
        return value


# model that will be used when returning data of user in api response
class User(UserBase):
    id: int
    is_active: bool

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
    # but an ORM model (or any other arbitrary object with attributes).
    # this should be set to True for models that will be used for reading data
    # Without orm_mode, if you returned a SQLAlchemy model from your path operation,
    # it wouldn’t include the relationship data.

    class Config:
        orm_mode = True

