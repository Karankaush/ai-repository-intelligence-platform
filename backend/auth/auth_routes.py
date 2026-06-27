from fastapi import APIRouter, Depends

from auth.auth_service import register_user, login_user
from auth.schemas import RegisterRequest, LoginRequest
from auth.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
async def register(data: RegisterRequest):

    return await register_user(
        data.name,
        data.email,
        data.password
    )


@router.post('/login')
async def login(data : LoginRequest):
    return await login_user(data.email, data.password)
    


@router.get("/me")
async def get_me(current_user=Depends(get_current_user)):
    return current_user




