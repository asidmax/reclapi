from fastapi import APIRouter

router = APIRouter(
    prefix='/location'
)


@router.get('/')
def index():
    return {'message': 'Good'}
