from fastapi import APIRouter

router = APIRouter(
    prefix="/songs",
    tags=["songs"]
)

@router.get("/{songname}")
async def getSongBySongname():
    return [{"songname": "Etrian Oddysey"}]


