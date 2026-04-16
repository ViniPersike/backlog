from operator import truediv
from .connection import get_connection

con = get_connection()
cursor = con.cursor()

def check_login(username:str, password:str):

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    if result:
        return True, result[0]
    return False, None

def check_if_game_already_added(id_check):
    select_query = "SELECT id, rawg_id FROM games WHERE rawg_id = %s"
    cursor.execute(select_query, (id_check,))
    result = cursor.fetchone()

    if result:
        return True
    return False

def add_game_to_database(rawg_id, name, release_date):
    insert_query = "INSERT INTO games (rawg_id, name, release_date) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (rawg_id, name, release_date))
    con.commit()

def add_game_no_status(user_id, game_id):

    insert_query = "INSERT INTO user_backlog (user_id, game_id) VALUES (%s, %s)"
    cursor.execute(insert_query, (user_id, game_id))
    con.commit()

def get_game_id(game_rawg_id):
    select_query = "SELECT id FROM games WHERE rawg_id = %s"
    cursor.execute(select_query, (game_rawg_id,))
    result = cursor.fetchone()

    return result

def show_user_backlog(user_id):
    select_query = """SELECT 
                      game_id,
                      user_review,
                      game_status,
                      game_rating,
                      playtime,
                      date_started,
                      date_finished
                      FROM user_backlog WHERE user_id = %s"""
    cursor.execute(select_query, (user_id,))
    result = cursor.fetchall()

    print("Game: | review | status | rating | playtime | date started | date finished")
    for game in result:
        #print(game)
        cursor.execute("SELECT name FROM games WHERE id = %s", (game[0],))
        game_title = cursor.fetchone()
        print(game_title[0], end=" | ")
        for i in range(1, len(game)):
            print(game[i], end=" | ")
        print()