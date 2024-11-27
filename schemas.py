from pydantic import BaseModel, EmailStr
from typing import Optional

# Request model for user registration
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

# Response model for user details
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True

# Request model for login
class UserLogin(BaseModel):
    username: str
    password: str

# Token response model
class Token(BaseModel):
    access_token: str
    token_type: str
