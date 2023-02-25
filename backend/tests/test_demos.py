import pytest

from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)


@pytest.mark.anyio
async def test_read_demos(async_client) -> None:
    res = await async_client.get("/v1/demos", follow_redirects=True)
    assert res.status_code == HTTP_200_OK
    assert res.json() == []


@pytest.mark.anyio
async def test_invalid_input_raises_error(async_client) -> None:
    res = await async_client.post("/v1/demos", json={}, follow_redirects=True)
    assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.anyio
async def test_create_new_demo(async_client) -> None:
    json_data = {
        "name": "New Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T21:00:36+01:00",
    }
    res = await async_client.post("/v1/demos", json=json_data, follow_redirects=True)
    assert res.status_code == HTTP_201_CREATED
    assert res.json() == {
        "id": 1,
        "name": "New Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T20:00:36+00:00",  # utc
    }


@pytest.mark.anyio
async def test_read_demo(async_client) -> None:
    res = await async_client.get("/v1/demos/1", follow_redirects=True)
    assert res.status_code == HTTP_200_OK
    assert res.json() == {
        "id": 1,
        "name": "New Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T20:00:36+00:00",  # utc
    }


@pytest.mark.anyio
async def test_patch_demo(async_client) -> None:
    json_data = {
        "id": 1,
        "name": "New altered Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T21:00:36+01:00",
    }
    res = await async_client.patch("/v1/demos/1", json=json_data, follow_redirects=True)
    assert res.status_code == HTTP_200_OK
    assert res.json() == {
        "id": 1,
        "name": "New altered Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T20:00:36+00:00",  # utc
    }


@pytest.mark.anyio
async def test_remove_demo(async_client) -> None:
    json_data = {
        "id": 1,
        "name": "New altered Demo",
        "decimal_value": 3.14,
        "entry_date": "2023-02-18T21:00:36+01:00",
    }
    # TODO delete requests w/ payload are discouraged, refactor this
    # res = await async_client.delete("/v1/demos/1", follow_redirects=True)
    res = await async_client.request(
        method="DELETE", url="/v1/demos/1", json=json_data, follow_redirects=True
    )
    assert res.status_code == HTTP_200_OK


@pytest.mark.anyio
async def test_invalid_id_raises_error(async_client) -> None:
    res = await async_client.get("/v1/demos/1", follow_redirects=True)
    assert res.status_code == HTTP_404_NOT_FOUND
