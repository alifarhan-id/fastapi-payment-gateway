from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserOut
from fastapi import Depends
from services.user_services import UserServices

from models.user_model import User



invoice_router = APIRouter()

@invoice_router.get('/invoices', summary="get list invoice", response_model=UserOut)
async def invoices(data: UserAuth):
    pass


@invoice_router.get('/invoices/{id}', summary="get details invoice by id", response_model=UserOut)
async def invoices(data: UserAuth):
    pass


@invoice_router.delete('/invoices/{id}', summary="delete invoice by id", response_model=UserOut)
async def invoices(data: UserAuth):
    pass


@invoice_router.post('/invoices', summary="create invoice", response_model=UserOut)
async def invoices(data: UserAuth):
    pass


@invoice_router.post('/invoices/send/{id}', summary="send invoice", response_model=UserOut)
async def invoices(data: UserAuth):
    pass


@invoice_router.put('/invoices/{id}', summary="edit invoice", response_model=UserOut)
async def invoices(data: UserAuth):
    pass