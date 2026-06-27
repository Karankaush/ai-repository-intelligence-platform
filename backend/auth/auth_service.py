from fastapi import HTTPException
from auth.hash import hash_password
from auth.jwt import create_access_token
from auth.hash import verify_password



from database.mongodb import db

users_collection = db["users"]

async def register_user(name: str, email: str, password: str):

    existing_user = await users_collection.find_one({"email": email})

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    user = {
        "name": name,
        "email": email,
        "password": hash_password(password)
    }

    await users_collection.insert_one(user)

    return {
        "message": "User registered successfully"
    }


async def login_user(email : str, password : str):
    
    user = await users_collection.find_one({"email" : email})
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not exist",
            more_info="Please register first"
        )
    
    if not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    
    access_token = create_access_token({
        "user_id" : str(user["_id"]),
        "email" : user['email']
    })

    return {
         "user" : {user["name"], user["email"]},
        "access_token": access_token,
        "token_type": "bearer"
    }




