from typing import Optional
from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    name: str = Field(index=True)
    email: str = Field(index=True, unique=True)


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    name: str
    email: str

class UserUpdate(UserBase):
    name: Optional[str] = None
    email: Optional[str] = None

class UserPublic(UserBase):
    name: str
    model_config = {
        "from_attributes": True
    }
   