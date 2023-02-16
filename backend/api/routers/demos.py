import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from api import schemas
from api.crud.demos import create_demo, delete_demo, get_demo, get_demos, update_demo
from api.db.database import get_db


logger = logging.getLogger("fastapi-vue")

router = APIRouter(
    prefix="/demos",
    tags=["demos"],
    responses={
        400: {"description": "Bad request"},
        404: {"description": "Not found"},
    },
)


@router.get("/", response_model=List[schemas.Demo])
async def read_demos(db: AsyncSession = Depends(get_db)):
    demos = await get_demos(db)
    return demos


@router.get("/{demo_id}", response_model=schemas.Demo)
async def read_demo(demo_id: int, db: AsyncSession = Depends(get_db)):
    db_demo = await get_demo(db=db, demo_id=demo_id)
    if db_demo is None:
        raise HTTPException(status_code=404, detail="Demo not found")
    return db_demo


@router.post("/", response_model=schemas.Demo, status_code=201)
async def create_new_demo(demo: schemas.DemoCreate, db: AsyncSession = Depends(get_db)):
    return await create_demo(db=db, demo=demo)


@router.patch("/{demo_id}", response_model=schemas.Demo)
async def patch_demo(
    demo_id: int, demo: schemas.Demo, db: AsyncSession = Depends(get_db)
):
    if demo_id != demo.id:
        raise HTTPException(status_code=400, detail="Demo id's not matching")
    return await update_demo(db=db, demo=demo)


@router.delete("/{demo_id}", response_model=schemas.Demo)
async def remove_demo(
    demo_id: int, demo: schemas.Demo, db: AsyncSession = Depends(get_db)
):
    if demo_id != demo.id:
        raise HTTPException(status_code=400, detail="Demo id's not matching")
    return await delete_demo(db=db, demo=demo)
