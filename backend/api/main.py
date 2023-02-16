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

app = FastAPI()
app.include_router(demos.router, prefix="/v1")


@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await async_engine.dispose()


@app.get("/")
async def root():
    logger.info("Hello World")
    return {"message": "Hello World"}
