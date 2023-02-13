import logging

from fastapi import FastAPI
from rich.logging import RichHandler

from api.db.database import database
from api.routers import demos


FORMAT = "%(message)s"
logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S", handlers=[RichHandler()]
)

logger = logging.getLogger("fastapi-demo")

app = FastAPI()
app.include_router(demos.router, prefix="/v1")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def root():
    logger.info("Hello World")
    return {"message": "Hello World"}
