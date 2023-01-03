from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserOut
from fastapi import Depends
from services.user_services import UserServices

from models.user_model import User



otp_router = APIRouter()

@otp_router.post('/otp/generate', summary="generate otp", response_model=UserOut)
async def generate_otp(data: UserAuth):
    pass

@otp_router.post('/otp/verify', summary="verify otp", response_model=UserOut)
async def verify_otp(data: UserAuth):
    pass

@otp_router.delete('/otp', summary="get otp", response_model=UserOut)
async def verify_otp(data: UserAuth):
    pass