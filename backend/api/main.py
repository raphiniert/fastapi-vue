import logging

from fastapi import FastAPI
from rich.logging import RichHandler

from api.routers import demos
from api.db.database import Base, async_engine


FORMAT = "%(message)s"
logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S", handlers=[RichHandler()]
)

logger = logging.getLogger("fastapi-demo")

app = FastAPI(
    title="Fast API Vue Demo",
    description="Demo project for testing fast api and vuejs.",
    version="0.0.1",
)
app.include_router(demos.router, prefix="/v1")


@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await async_engine.dispose()
