from fastapi import APIRouter
from services import root

router = APIRouter()

router.include_router(root.root, prefix='/root', tags=["root"])


