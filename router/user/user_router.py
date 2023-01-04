import sys
from fastapi import APIRouter, HTTPException, status, Request, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schemas.user_schema import RegisterSchema
from schemas.response import ResponseData
from bin.database.database import Database
from bin.utils.utils import get_hashed_password, generate_secret_key, generate_oauth_access_token_id

from models.user_model import UserModel, OauthAccessTokenModel, OauthClientModel
#from app.api.deps.user_deps import get_current_user


user_router = APIRouter()

db = Database()
engine = db.get_db_connection()
session = db.get_db_session(engine)

@user_router.post('/register', summary="Create new user")
async def create_user(req: RegisterSchema, response: Response):

    try:
        user = UserModel()
        user.first_name = req.first_name
        user.last_name = req.last_name
        user.email = req.email,
        user.password = get_hashed_password(req.password)
        user.created_by = req.created_by
        user.status_id = req.status_id
        secret = generate_secret_key(req.email)
        
        session.add(user)
        session.flush()
        session.refresh(user, attribute_names=['id']) #refresh token and returning user.id
        # data = {"user_id": user.id}
        session.commit()
        session.close()

        oauth_client = OauthClientModel()
        oauth_client.id = user.id
        oauth_client.user_id = user.id
        oauth_client.secret = secret
        oauth_client.name = 'Monateri APP'
        oauth_client.personal_access_client = 1
        oauth_client.revoked = 0
        oauth_client.password_clinet = 0
        oauth_client.redirect = "https://app.monateri.bio/"

        session.add(oauth_client)
        session.flush()
        session.commit()
        session.close()

        oauth_access_token = OauthAccessTokenModel()
        oauth_access_token.id = generate_oauth_access_token_id(req.email)
        oauth_access_token.user_id = user.id
        oauth_access_token.client_id = 1
        oauth_access_token.name = "Monateri APP"
        oauth_access_token.scopes = ""
        oauth_access_token.revoked = 0
        session.add(oauth_access_token)
        session.flush()
        session.commit()
        session.close()


        
        client_id = session.query(OauthAccessTokenModel).filter(OauthAccessTokenModel.user_id == user.id).first()

        response_data = {       
            'client_id': client_id.id,
            'client_secret': secret
        }
        
        response.status_code=status.HTTP_201_CREATED
        return ResponseData(status.HTTP_201_CREATED, True, None, response_data)

    except IntegrityError:
        session.rollback()
        response.status_code=status.HTTP_400_BAD_REQUEST
        return ResponseData(status.HTTP_400_BAD_REQUEST, False, "Bad Request", None)

    except Exception as ex:
        session.rollback()
        print(ex)
        response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        return ResponseData(status.HTTP_500_INTERNAL_SERVER_ERROR, False, ex, None)