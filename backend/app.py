from fastapi import FastAPI
from database.mongodb import db
from auth.jwt import create_access_token, verify_access_token
from auth.auth_routes import router as auth_router

from repository.repository_routes import router as repository_router

app = FastAPI(
    title="AI Repository Intelligence Platform",
    version= "0.1.0"
)

app.include_router(repository_router)
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
    

