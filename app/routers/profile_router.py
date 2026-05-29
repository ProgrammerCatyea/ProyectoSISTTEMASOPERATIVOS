from fastapi import APIRouter
from app.services.steam_service import get_steam_profile

router = APIRouter(
    prefix="/profile",
    tags=["Profiles"]
)

@router.get("/{steam_id}")
def profile(steam_id: str):

    steam_data = get_steam_profile(steam_id)

    if not steam_data:
        return {
            "error": "Perfil no encontrado"
        }

    return {
        "steam_profile": steam_data
    }