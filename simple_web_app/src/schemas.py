from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    password: str

class Item(UserBase):
    id: int

    class Config:
        orm_mode = True