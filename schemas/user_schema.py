from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    first_name: str = Field(..., description="First Name")
    last_name: str = Field(..., description="Last Name")
    email: EmailStr = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")
    status_id: int
    created_at: int


class UserOut(BaseModel):
    user_id: UUID
    first_name: str
    last_name: Optional[str]
    email: EmailStr
    password: Optional[str]
    status_id: int
    created_at: int

