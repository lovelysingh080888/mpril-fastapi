# config.py
import os
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from dotenv import load_dotenv

def configure_database():
    load_dotenv()
    MONGODB_URL = os.getenv('MONGODB_URL')

    async def configure():
        client = AsyncIOMotorClient(MONGODB_URL)
        engine = AIOEngine(client=client, database='workout_db')
        return engine
    
    return configure
