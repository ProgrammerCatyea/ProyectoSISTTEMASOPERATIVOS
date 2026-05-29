import requests
from app.config.settings import STEAM_API_KEY

def get_steam_profile(steam_id):

    # =========================
    # Perfil del usuario
    # =========================
    profile_url = (
        f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"
        f"?key={STEAM_API_KEY}&steamids={steam_id}"
    )

    profile_response = requests.get(profile_url)
    profile_data = profile_response.json()

    players = profile_data["response"]["players"]

    if not players:
        return None

    player = players[0]

   
    games_url = (
        f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
        f"?key={STEAM_API_KEY}&steamid={steam_id}"
        f"&include_appinfo=true"
        f"&include_played_free_games=true"
    )

    games_response = requests.get(games_url)
    games_data = games_response.json()

    games = games_data.get("response", {}).get("games", [])

    
    top_game = None

    if games:
        most_played = max(games, key=lambda game: game.get("playtime_forever", 0))

        top_game = {
            "name": most_played.get("name"),
            "hours": round(most_played.get("playtime_forever", 0) / 60, 2)
        }

  
    recent_games = []

    for game in games[:5]:
        recent_games.append({
            "name": game.get("name"),
            "hours": round(game.get("playtime_forever", 0) / 60, 2)
        })

    return {
        "username": player.get("personaname"),
        "avatar": player.get("avatarfull"),
        "profile_url": player.get("profileurl"),
        "status": player.get("personastate"),
        "top_game": top_game,
        "recent_games": recent_games,
        "total_games": len(games)
    }