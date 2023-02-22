import pytest

from httpx import AsyncClient
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from api.main import app


@pytest.mark.asyncio
async def test_read_demos() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/v1/demos", follow_redirects=True)
    assert res.status_code == HTTP_200_OK
    assert res.json() == []


@pytest.mark.asyncio
async def test_invalid_input_raises_error() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post("/v1/demos", json={})
    assert res.status_code != HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_create_new_demo() -> None:
    json_data = {
        "name": "New Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T21:00:36+01:00",
    }
    async with AsyncClient(
        app=app, base_url="http://test", follow_redirects=True
    ) as ac:
        res = await ac.post("/v1/demos", json=json_data, follow_redirects=True)
    assert res.status_code == HTTP_201_CREATED
    assert res.json() == {
        "id": 1,
        "name": "New Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T20:00:36+00:00",  # utc
    }


@pytest.mark.asyncio
async def test_read_demo() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/v1/demos/1", follow_redirects=True)
    assert res.status_code == HTTP_200_OK


@pytest.mark.asyncio
async def test_patch_demo() -> None:
    json_data = {
        "id": 1,
        "name": "New altered Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T21:00:36+01:00",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.patch("/v1/demos/1", json=json_data, follow_redirects=True)
    assert res.status_code == HTTP_200_OK
    assert res.json() == {
        "id": 1,
        "name": "New altered Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T20:00:36+00:00",  # utc
    }


@pytest.mark.asyncio
async def test_remove_demo() -> None:
    json_data = {
        "id": 1,
        "name": "New altered Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T21:00:36+01:00",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # TODO delete requests w/ payload are discouraged, refactor this
        # res = await ac.delete("/v1/demos/1", follow_redirects=True)
        res = await ac.request(
            method="DELETE", url="/v1/demos/1", json=json_data, follow_redirects=True
        )
    assert res.status_code == HTTP_200_OK
