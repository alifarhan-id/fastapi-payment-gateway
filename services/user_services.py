from typing import Optional
from uuid import UUID
from schemas.user_schema import UserAuth
from models.user_model import User
from bin.utils.utils import get_hashed_password
import pymongo

# from schemas.user_schema import UserUpdate


class UserServices:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.password,
                    password=get_hashed_password(user.password),
                    status_id=user.status_id,
                    created_at=user.created_at
                )
        await user_in.save()
        return user_in
