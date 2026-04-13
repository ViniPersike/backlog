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