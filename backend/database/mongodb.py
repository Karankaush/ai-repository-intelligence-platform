import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

try:
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    db = client[os.getenv("DATABASE_NAME")]
    print("Connected to MongoDB successfully")




except Exception as e:
    print("Error connecting to MongoDB:", e)
    raise e



