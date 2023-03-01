from fastapi import APIRouter
from .operations import router as oper
from .location import router as location
from .auth import router as auth


router = APIRouter()
router.include_router(auth)
router.include_router(oper)
router.include_router(location)
