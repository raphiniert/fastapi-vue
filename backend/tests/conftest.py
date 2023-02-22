import asyncio
import pytest

from fastapi.testclient import TestClient
from typing import Generator

from api.db.database import AsyncSessionLocal
from api.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield AsyncSessionLocal()


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
