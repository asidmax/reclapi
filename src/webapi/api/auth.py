from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from webapi.models.auth import Token, CreateUser, User
from webapi.services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth'
)


@router.post('/sing-up', response_model=Token)
def sing_up(
        user_data: CreateUser,
        auth_service: AuthService = Depends()
):
    return auth_service.register_new_user(user_data)


@router.post('/sing-in', response_model=Token)
def sing_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends()
):
    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password
    )


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user
