from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from api.core.config import settings


DATABASE_URL = f"postgresql+asyncpg://{settings.db_user}:{settings.db_password.get_secret_value()}@{settings.db_server}:{settings.db_port}/{settings.db_db}"

async_engine = create_async_engine(
    DATABASE_URL,
    # echo=True,
)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
