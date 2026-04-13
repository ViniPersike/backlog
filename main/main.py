from database.database import check_login
from database.init import init_db
from database import *
from generateHTML import generate_html
from menus import *
import webbrowser

init_db()



username_login, password_login = menu_login()
success, id = check_login(username_login, password_login)

if success:
    print("Login bem sucedido.")
else:
    print("Usuário não cadastrado.")