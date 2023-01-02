from fastapi import APIRouter



root = APIRouter()

@root.get('/', summary="check connection to kasinvoice")
async def root_test():
    return {"message": "pong"}