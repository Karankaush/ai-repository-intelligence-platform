from fastapi import FastAPI
from database.mongodb import db

app = FastAPI(
    title="AI Repository Intelligence Platform",
    version= "0.1.0"
)

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