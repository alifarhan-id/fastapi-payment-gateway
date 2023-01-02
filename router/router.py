from fastapi import APIRouter
from router.root import root
from router.user import user_router

router = APIRouter()

router.include_router(root.root, prefix='/root', tags=["root"])
router.include_router(user_router.user_router, prefix='/auth', tags=["auth"])


