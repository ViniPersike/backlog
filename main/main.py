from database.database import check_login, add_game_no_status, check_if_game_already_added, add_game_to_database, \
    get_game_id
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
        success, user_id = check_login(username_login, password_login)

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

                    while True:
                        try:
                            game_opt = int(input("Qual jogo deseja inserir no seu backlog? [Digite 0 para cancelar a operação]: "))
                        except ValueError as e:
                            print("Informe um número.")
                            continue

                        if 1 <= game_opt <= 5:
                            #To do add game to the database
                            #check if the game has already been added to the database
                            game_rawg_id = lista_jogos[game_opt-1]['id']
                            game_name = lista_jogos[game_opt-1]['name']
                            game_release_date = lista_jogos[game_opt-1]['released']

                            if check_if_game_already_added(game_rawg_id):
                                game_id = get_game_id(game_rawg_id)
                                add_game_no_status(user_id, game_id)
                                print("Game added to the user backlog")
                                break
                            else:
                                add_game_to_database(game_rawg_id, game_name, game_release_date)
                                print("Game added to database")
                                game_id = get_game_id(game_rawg_id)
                                add_game_no_status(user_id, game_id)
                                print("Game added to user backlog")
                                break
                        elif game_opt == 0:
                            break
                        else:
                            print("Opção inválida.")
                            continue

                elif opt == 2:
                    pass
                else:
                    print("Informe uma opção válida.")
        else:
            print("Usuário não cadastrado.")
    else:
        print("Opção inválida.")