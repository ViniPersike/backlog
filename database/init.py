from .connection import get_connection

con = get_connection()
cursor = con.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games(
        id serial PRIMARY KEY,
        rawg_id INTEGER UNIQUE,
        name TEXT,
        release_date DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT 
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_backlog(
        user_id INTEGER,
        game_id INTEGER,
        user_review TEXT,
        game_status TEXT,
        game_rating REAL,
        playtime INTEGER,
        date_started DATE,
        date_finished DATE,
        
        PRIMARY KEY (user_id, game_id),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (game_id) REFERENCES games(id)
    )
    """)
    con.commit()