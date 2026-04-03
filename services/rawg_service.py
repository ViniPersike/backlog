from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.rawg.io/api/games"

def search_games(game_title: str):
    params = {
        "key": API_KEY,
        "search": game_title
    }

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        raise Exception("API ERROR")

    filtered_games = []

    for i, game in enumerate(data["results"][:5]):
        filtered_games.append({
            "option": i+1,
            "id": game["id"],
            "name": game["name"],
            "released": game["released"]
        })

    return filtered_games