from fastapi import APIRouter
from .operations import router as oper


router = APIRouter()
router.include_router(oper)
