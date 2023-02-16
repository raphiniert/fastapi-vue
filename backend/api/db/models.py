import logging

from sqlalchemy import Column, DECIMAL, DateTime, func, Integer, String

from api.db.database import Base

logger = logging.getLogger("fastapi-demo")


class Demo(Base):
    # Table settings
    __tablename__ = "demos"

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    decimal_value = Column(DECIMAL, nullable=False)
    entry_date = Column(DateTime(timezone=True), nullable=False, default=func.now())
