from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    


class UserCreate(UserBase):
    password: str
    role: Optional[str] = "user"  # Default role is "user"


class UserSchema(UserBase):
    id: int
    role: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "john_doe",
                "email": "sarrsindian@gmail.com",
                "role": "user",
            }
        }