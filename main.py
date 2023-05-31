from bib import realizar_login, cadastrar_usuario

while(True):
    opcao = int(input('Insira 1 para login, 2 para cadastro: '))
    if opcao == 1:
        realizar_login()
        break
    elif opcao == 2:
        cadastrar_usuario()

