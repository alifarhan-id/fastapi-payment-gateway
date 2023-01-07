from datetime import datetime
from fastapi import Depends, HTTPException, status, Response

from fastapi.security import OAuth2PasswordBearer
from bin.settings.settings import settings
from models.user_model import UserModel as User
from jose import jwt
from pydantic import ValidationError

from schemas.auth_schema import TokenPayload
from bin.database.database import Database

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)

db = Database()
engine = db.get_db_connection()
session= db.get_db_session(engine)

def ResponseAuth(statusCode, success, error, data):
    return {
        "statusCode": statusCode,
        "success": success,
        "error": error,
        "data": data,
    }

async def get_current_user(res: Response, token: str = Depends(reuseable_oauth)) -> User:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            return ResponseAuth(401, False, "Token Expired", None)
    except(jwt.JWTError, ValidationError):
        return ResponseAuth(401, False, "Could not validate credentials", None)
        
        
    user = session.query(User).filter(User.email == token_data.sub).first()
    
    if not user:
         return ResponseAuth(404, False, "Could not validate credentials", None)


    return user
