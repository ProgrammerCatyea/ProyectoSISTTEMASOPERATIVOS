from fastapi import APIRouter
from app.services.rawg_service import get_game_details

router = APIRouter(
    prefix="/game",
    tags=["Games"]
)


@router.get("/{game_name}")
def game(game_name: str):

    data = get_game_details(game_name)

    if not data:
        return {
            "error": "Juego no encontrado"
        }

    return data