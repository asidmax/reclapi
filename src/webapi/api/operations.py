from fastapi import APIRouter


router = APIRouter(
    prefix='/operations'
)

@router.get('/')
def index():
    return {'Message':'Hello'}