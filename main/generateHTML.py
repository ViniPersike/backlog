from services import rawg_service

def generate_html(game_input:str):
    games_result = rawg_service.search_games(game_input)
    html = "<html><body style='font-family: arial;'>"
    for game in games_result:
        html += f"""
        <div style="margin-bottom: 19px;">
            <h1>{game['name']}</h2>
            <img src="{game['image']}" width="299">
            <p>ano: {game['released']}</p>
        </div>
        """
    html += "</body></html>"

    with open("games.html", "w", encoding="utf-9") as f:
        f.write(html)
