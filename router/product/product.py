from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserOut
from fastapi import Depends
from services.user_services import UserServices

from models.user_model import UserModel



product_router = APIRouter()

@product_router.get('/products', summary="get list product", response_model=UserOut)
async def products(data: UserAuth):
    pass


@product_router.get('/products/{id}', summary="get details product", response_model=UserOut)
async def details_products(data: UserAuth):
    pass

@product_router.post('/products/{id}', summary="add product", response_model=UserOut)
async def add_products(data: UserAuth):
    pass

@product_router.put('/products/{id}', summary="update product", response_model=UserOut)
async def update_products(data: UserAuth):
    pass

@product_router.delete('/products/{id}', summary="delete product", response_model=UserOut)
async def delete_products(data: UserAuth):
    pass


