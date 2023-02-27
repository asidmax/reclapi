from fastapi import APIRouter
from .operations import router as oper
from .location import router as location


router = APIRouter()
router.include_router(oper)
router.include_router(location)
