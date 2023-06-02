class SistemaAutenticacao:
    def cadastrar_usuario(self):
        usuario = input('Insira seu nome de usuário: ')
        senha = input('Insira sua senha: ')

        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(usuario + " " + senha + "\n")

        print('Usuário cadastrado com sucesso!')

    def realizar_login(self):
        usuario = input('Insira seu nome de usuário: ')
        senha = input('Insira sua senha: ')

        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                credenciais = linha.strip().split(" ")
                if usuario == credenciais[0] and senha == credenciais[1]:
                    print("Login bem sucedido!")
                    return
            print('Informações inválidas')

sistema = SistemaAutenticacao()
sistema.cadastrar_usuario()
sistema.realizar_login()