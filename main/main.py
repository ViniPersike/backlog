from database.database import check_login
from database.init import init_db
from database import *
from generateHTML import generate_html
from menus import *
from services.rawg_service import search_games
from time import sleep
import webbrowser

init_db()


while True:
    print("1- Login")
    print("0- Sair")
    try:
        opt = int(input("Opção: "))
    except ValueError as e:
        print("Informe um número")
        continue

    if opt == 0:
        break
    elif opt == 1:
        username_login, password_login = login_menu()
        success, id = check_login(username_login, password_login)

        if success:
            print("Login bem sucedido.")
            sleep(0.7)
            while True:
                main_menu()
                try:
                    opt = int(input("Opção: "))
                except ValueError as e:
                    print("Informe um número.")

                if opt == 1:
                    searching_game_title = str(input("Título do jogo: "))
                    lista_jogos = search_games(searching_game_title)
                    mostrar_jogos(lista_jogos)

                    try:
                        game_opt = int(input("Qual jogo deseja inserir no seu backlog? [Digite 0 para cancelar a operação]: "))
                    except ValueError as e:
                        print("Informe um número.")
                        continue

                    if game_opt == 1:
                        #To do add game to the database
                        pass
                    if game_opt == 0:
                        continue

                elif opt == 2:
                    pass
                else:
                    print("Informe uma opção válida.")
        else:
            print("Usuário não cadastrado.")
    else:
        print("Opção inválida.")