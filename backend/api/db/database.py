import databases

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.core.config import settings


DATABASE_URL = f"postgresql+asyncpg://{settings.db_user}:{settings.db_password.get_secret_value()}@{settings.db_server}:{settings.db_port}/{settings.db_db}"

database = databases.Database(DATABASE_URL)
