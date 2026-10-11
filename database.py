import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)
from sqlalchemy.orm import DeclarativeBase

#load .env
load_dotenv()

#Database  configuration
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "")
DB_PORT = os.getenv("DB_PORT", "")
DB_NAME=os.getenv(
    "DB_NAME" ,
    ""    
)

#Database  URL

DATABASE_URL=(
    f"mysql+asyncmy://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"   
)

#async engine
engine=create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

#Async session

AsyncSessionLocal=async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

#Base

class Base(DeclarativeBase):
    pass

# Provide a database session to API endpoints
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


