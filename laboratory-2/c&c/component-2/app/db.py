import motor.motor_asyncio
import os

client = None
db = None

async def init_db():
    global client, db
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_HOST"])
    db = client[os.environ["DB_NAME"]]

def get_collection():
    return db["items"]
