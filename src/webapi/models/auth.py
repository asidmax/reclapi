from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    username: str
    email: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class CreateUser(BaseUser):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
