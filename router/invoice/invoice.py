from fastapi import APIRouter, HTTPException, status, Request, Response
from schemas.user_schema import UserAuth, UserOut
from fastapi import Depends
from services.user_services import UserServices
from bin.deps.deps import get_current_user
from models.user_model import UserModel as User

from models.user_model import UserModel



invoice_router = APIRouter()

@invoice_router.get('/invoices', summary="get list invoice", response_model=UserOut)
async def invoices(data: UserAuth):
    pass


@invoice_router.get('/invoices/{id}', summary="get details invoice by id")
async def invoices(req: Request, res:Response, current_user: User = Depends(get_current_user) ):
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