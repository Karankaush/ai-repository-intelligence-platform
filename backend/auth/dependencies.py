from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from auth.jwt import verify_access_token
from database.mongodb import db

security = HTTPBearer()

users_collection = db["users"]


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    user = await users_collection.find_one(
        {"email": payload["email"]},
        {"password": 0},
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    user["_id"] = str(user["_id"])

    return user