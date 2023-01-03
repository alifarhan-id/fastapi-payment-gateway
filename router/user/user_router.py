from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserOut
from fastapi import Depends
from services.user_services import UserServices

from models.user_model import User
#from app.api.deps.user_deps import get_current_user


user_router = APIRouter()

@user_router.post('/register', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    pass
