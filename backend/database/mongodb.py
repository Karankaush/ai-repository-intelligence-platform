import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

try:
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    db = client[os.getenv("DATABASE_NAME")]
    print("Connected to MongoDB successfully")
    print(os.getenv("MONGODB_URI"))


    print("MONGO_URI =", os.getenv("MONGO_URI"))
    print("MONGODB_URI =", os.getenv("MONGODB_URI"))
    print("DATABASE_NAME =", os.getenv("DATABASE_NAME"))



except Exception as e:
    print("Error connecting to MongoDB:", e)
    raise e



