from passlib.context import CryptContext
import hashlib
import hmac
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

from bin.settings.settings import settings


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def generate_secret_key(key: str) -> str:
    payload = settings.JWT_SECRET_KEY
    secret_key = hmac.new(key.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return secret_key

def generate_oauth_access_token_id(key: str) -> str:
    payload = "@!WE$%#@@@@@@@@DS@"
    secret_key = hmac.new(key.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return secret_key
