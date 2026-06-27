from fastapi import HTTPException
from auth.hash import hash_password


from database.mongodb import db

users_collection = db["users"]

async def register_user(name : str, email: str, password: str):
    existing_user = await users_collection.find_one({"email" : email})

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exist"
        )
    
    user = {
        "name" : name,
        "email" : email,
        password : hash_password(password)
    }

    await users_collection.insert_one(user)

    return{
       "message" : "User registered successfully" 
    }