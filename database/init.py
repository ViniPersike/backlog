from .connection import get_connection

con = get_connection()
cursor = con.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games(
        id serial PRIMARY KEY,
        rawg_id INTEGER UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT 
    )
    """)

    con.commit()