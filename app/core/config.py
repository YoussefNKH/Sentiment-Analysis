 # app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv

class Settings:
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DB_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
    DB_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")
    DB_NAME = os.getenv("MONGO_DB_NAME", "mydatabase")
    TWITTER_BEARER_TOKEN= os.getenv("TWITTER_BEARER_TOKEN", "")
settings = Settings() 