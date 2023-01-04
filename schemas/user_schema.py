from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, validator
from models.user_model import UserModel


class UserAuth(BaseModel):
    pass

class RegisterSchema(BaseModel):
    first_name: str 
    last_name: str 
    email: EmailStr
    password: str 
    status_id: int
    created_by: int 


class UserOut(BaseModel):
    user_id: UUID
    first_name: str
    last_name: Optional[str]
    email: EmailStr
    password: Optional[str]
    status_id: int
    created_at: int

