from fastapi import FastAPI
from database.mongodb import db
from auth.jwt import create_access_token, verify_access_token
from auth.auth_routes import router as auth_router


app = FastAPI(
    title="AI Repository Intelligence Platform",
    version= "0.1.0"
)

app.include_router(auth_router)






@app.get('/')
async def home():
    return {"message": "Welcome to the AI Repository Intelligence Platform!"}


@app.get("/health")
async def health():
    try:
        await db.command("ping")
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }
    

@app.get('/token')
async def generate_token():
    token = create_access_token({"email" : "karan@gmail.com" ,"role" : "user"})
    return{
        "token" : token
    }


@app.get('/verify')
async def verify_token():

    token = create_access_token({"email" : "karan@gmail.com", "role" : "user"})
    payload = verify_access_token(token)
    return {
        "status" : "token verified",
        "payload" : payload
    }

