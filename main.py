from bib import realizar_login, cadastrar_usuario

sistema = SistemaAutenticacao()

while True:
    opcao = int(input('Insira 1 para login, 2 para cadastro: '))
    if opcao == 1:
        sistema.realizar_login()
        break
    elif opcao == 2:
        sistema.cadastrar_usuario()
        break

