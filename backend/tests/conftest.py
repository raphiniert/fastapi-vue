import pytest
from fastapi.testclient import TestClient
from typing import Generator

from api.db.database import AsyncSessionLocal
from api.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield AsyncSessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
