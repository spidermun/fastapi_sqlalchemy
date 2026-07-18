
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import CONFIG
from sqlalchemy import text

db_url = f"postgresql+asyncpg://{CONFIG.POSTGRES_USER}:{CONFIG.POSTGRES_PASSWORD}@db/{CONFIG.POSTGRES_DB}"

engine = create_async_engine(url=db_url, echo=True)


async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'DATABASE Initialized'")
        result = await conn.execute(statement)