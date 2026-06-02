import requests
from app.config.settings import RAWG_API_KEY

def get_game_details(game_name: str):

    print("RAWG KEY:", RAWG_API_KEY)

    url = (
        f"https://api.rawg.io/api/games"
        f"?key={RAWG_API_KEY}"
        f"&search={game_name}"
    )

    print(url)

    response = requests.get(url)

    print(response.status_code)
    print(response.text[:500])

    if response.status_code != 200:
        return None

    data = response.json()

    if not data["results"]:
        return None

    game = data["results"][0]

    return {
        "name": game.get("name"),
        "rating": game.get("rating")
    }