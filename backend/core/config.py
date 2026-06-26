import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "AI Repository Intelligence Platform")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
    # DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    # HOST = os.getenv("HOST", "127.0.0.1")
    # PORT = int(os.getenv("PORT", 8000))

    MONGO_URI=os.getenv("MONGO_URI")
    DATABSE_NAME=os.getenv("DATABSE_NAME")


settings = Settings()