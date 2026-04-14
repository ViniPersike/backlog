def login_menu():
    current_user = str(input("Usuário: "))
    current_password = str(input("Senha: "))
    return current_user, current_password

def main_menu():
    print("1- Buscar jogo")
    print("2- Mostrar meu backlog")

def mostrar_jogos(lista_jogos):
    for k, v in enumerate(lista_jogos):
        print("="*25)
        print(f"{k+1}- {v['name']} - {v['released']}")