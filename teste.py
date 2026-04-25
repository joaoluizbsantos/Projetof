livros_disponiveis = [
    "Dom Casmurro",
    "1984",
    "O Pequeno Príncipe",
    "Senhor dos Anéis",
    "Harry Potter"
]

usuarios = [
   "joao",
   "jose"
]

livros_emprestados = []

def listar_usuarios():
    print("\nUsuários:")
    for i, nome in enumerate(usuarios, start=1):
        print(f"{i} - {nome}")
    print()

def cadastrar_usuarios():
    nome = input("Digite o nome do novo usuário: ")

    if not nome:
        print("Nome inválido.\n")
        return

    usuarios.append(nome)
    print(f"Usuário '{nome}' cadastrado com sucesso!\n")


def listar_livros():
    if not livros_disponiveis:
        print("\nNenhum livro disponível.\n")
        return

    print("\nLivros disponíveis:")
    for i, livro in enumerate(livros_disponiveis, start=1):
        print(f"{i} - {livro}")
    print()

def listar_emprestados():
    if not livros_emprestados:
        print("\nNenhum livro emprestado.\n")
        return

    print("\nLivros emprestados:")
    for i, livro in enumerate(livros_emprestados, start=1):
        print(f"{i} - {livro}")
    print()


def emprestimo():
    if not livros_disponiveis:
        print("Não há livros disponíveis.\n")
        return

    listar_usuarios()
    user = input("Digite o ID do usuário: ")

    if not user.isdigit() or not (1 <= int(user) <= len(usuarios)):
        print("Usuário inválido.\n")
        return

    listar_livros()

    escolha = input("Digite o número do livro: ")

    if escolha.isdigit():
        indice = int(escolha) - 1

        if 0 <= indice < len(livros_disponiveis):
            livro = livros_disponiveis.pop(indice)
            livros_emprestados.append(livro)

            print(f"\n{usuarios[int(user)-1]} pegou o livro: {livro}\n")
        else:
            print("\nNúmero inválido!\n")
    else:
        print("\nDigite um número válido!\n")

def devolucao():

    listar_usuarios()
    user = input("Digite o ID do usuário: ")

    if not user.isdigit() or not (1 <= int(user) <= len(usuarios)):
        print("Usuário inválido.\n")
        return

    if not livros_emprestados:
        print("Nenhum livro para devolver.\n")
        return

    listar_emprestados()

    escolha = input("Digite o número do livro que deseja devolver: ")

    if escolha.isdigit():
        indice = int(escolha) - 1

        if 0 <= indice < len(livros_emprestados):
            livro = livros_emprestados.pop(indice)
            livros_disponiveis.append(livro)
            print(f"\n{usuarios[int(user)-1]} devolveu o livro: {livro}\n")
        else:
            print("\nNúmero inválido!\n")
    else:
        print("\nDigite um número válido!\n")


def menu():
    while True:
        opcao = input(
            "Pressione o número desejado:\n\n"
            "1 - Listar livros disponíveis\n"
            "2 - Realizar empréstimo\n"
            "3 - Devolução\n"
            "4 - Listar livros emprestados\n"
            "5 - Listar Usuarios\n"
            "6 - Criar Usuario\n"
            "0 - Sair\n\n"
            "Opção: "
        )

        if opcao == '1':
            listar_livros()

        elif opcao == '2':
            emprestimo()

        elif opcao == '3':
            devolucao()

        elif opcao == '4':
            listar_emprestados()

        elif opcao == '5':
            listar_usuarios()

        elif opcao == '6':
            cadastrar_usuarios()

        elif opcao == '0':
            print("\nSaindo do sistema. Até mais!\n")
            break

        else:
            print("\nOpção inválida! Tente novamente.\n")


print("Olá, seja bem-vindo ao Sistema de Biblioteca!\n")
menu()