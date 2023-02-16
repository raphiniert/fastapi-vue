import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.db.models import Demo
from api import schemas

logger = logging.getLogger("fastapi-vue")


async def get_demo(db: AsyncSession, demo_id: int):
    query = select(Demo).where(Demo.id == demo_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_demos(db: AsyncSession):
    query = select(Demo)
    result = await db.execute(query)
    return result.scalars().all()


async def create_demo(db: AsyncSession, demo: schemas.DemoCreate):
    new_demo = Demo(
        name=demo.name, decimal_value=demo.decimal_value, entry_date=demo.entry_date
    )
    db.add(new_demo)
    # await db.flush()
    await db.commit()
    await db.refresh(new_demo)
    return new_demo


async def update_demo(db: AsyncSession, demo: schemas.Demo):
    db_demo = await get_demo(db=db, demo_id=demo.id)
    for field, value in demo:
        setattr(db_demo, field, value)
    db.add(db_demo)
    await db.commit()
    await db.refresh(db_demo)
    return db_demo
