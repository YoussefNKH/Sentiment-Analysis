# app/database/mongodb.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId



# DB Connection Variables
client = None
db = None

async def init_db():
    """Initialize the database connection"""
    global client, db
    