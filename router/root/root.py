from fastapi import APIRouter, Depends, Response, status



root = APIRouter()

@root.get('/', summary="check connection to kasinvoice")
async def root_test(response: Response):
    return {"message": "pong"}