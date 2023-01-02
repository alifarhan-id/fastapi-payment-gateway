from typing import Union
from beanie import init_beanie
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from bin.settings.settings import settings
from router.router import router
from models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """

    db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).kasinvoice

    await init_beanie(
        database=db,
        document_models=[
            User
        ]
    )
app.include_router(router, prefix=settings.API_V1_STR)


