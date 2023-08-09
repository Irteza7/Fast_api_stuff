from datetime import datetime
from pydantic import BaseModel, EmailStr, conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass



class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserOut

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None

class Vote(BaseModel):
    post_id : int
    dir: conint(ge=0, le=1)


