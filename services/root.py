from fastapi import APIRouter



root = APIRouter()

@root.get('/', summary="check connection to KASINVOICE")
async def root_test():
    return {"message": "pong"}
