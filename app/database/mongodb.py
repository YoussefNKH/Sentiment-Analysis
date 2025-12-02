# app/database/mongodb.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.core.config import settings


# DB Connection Variables
client = None
db = None

async def init_db():
    """Initialize the database connection"""
    global client, db

    mongodb_url = settings.MONGODB_URL
    #authentication
    username = settings.DB_USERNAME
    password = settings.DB_PASSWORD

# build the connection string with credentials
    if "://" in mongodb_url and "@" not in mongodb_url:
        # Add credentials if not already in the URL
        parts = mongodb_url.split("://")
        mongodb_url = f"{parts[0]}://{username}:{password}@{parts[1]}"
    print(f"Connecting to MongoDB at: {mongodb_url.replace(password, '****')}")
    client = AsyncIOMotorClient(mongodb_url)
    db_name = settings.DB_NAME
    db = client[db_name]
    print(f"Connected to database: {db_name}")
    return db
async def get_posts(limit=100):
    global db

    if db is None:
        await init_db()
    posts_cursor = db.posts.find().limit(limit)
    posts= await posts_cursor.to_list(length=limit)

    #convert ObjectId to string for JSON serialization
    for post in posts:
        post["_id"] = str(post["_id"])
    return posts