from fastapi import APIRouter

router = APIRouter()

router = APIRouter(
    prefix="/demos",
    tags=["demos"],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/")
async def read_demos():
    return {"read": "demos"}
