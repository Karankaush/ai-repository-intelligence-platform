from fastapi import APIRouter

from auth.auth_service import register_user
from auth.schemas import RegisterRequest

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