# Biblioteca virtual
# Projeto da faculdade (Anhanguera, 2025) - roda no terminal
# Cadastra, lista e pesquisa livros e gera um gráfico com a quantidade por gênero

# Biblioteca para criar o gráfico (instalar com: pip install matplotlib)
import matplotlib.pyplot as plt

# Lista que guarda todos os livros cadastrados.
# Cada livro é um dicionário com título, autor, gênero e quantidade.
biblioteca = []


def ler_quantidade(mensagem):
    """Lê um número inteiro maior ou igual a zero, repetindo até ser válido."""
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            # int() dá erro (ValueError) se o texto não for um número inteiro
            print("Digite um número inteiro.")
            continue  # volta ao início do while e pergunta de novo

        if valor >= 0:
            return valor
        print("A quantidade não pode ser negativa.")


# Função 1: Cadastrar livro
def cadastrar_livro():
    """Cadastra um livro na biblioteca com título, autor, gênero e quantidade disponível."""
    # strip() tira espaços sobrando no começo e no fim do texto
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor do livro: ").strip()
    genero = input("Digite o gênero do livro: ").strip()

    # não deixa cadastrar um livro sem título
    if not titulo:
        print("O título não pode ficar vazio.\n")
        return

    quantidade = ler_quantidade("Digite a quantidade disponível: ")

    # Cria um dicionário para guardar as informações do livro
    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "quantidade": quantidade,
    }

    # Adiciona o livro na lista principal
    biblioteca.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso! Quantidade disponível: {quantidade}\n")


# Função 2: Listar todos os livros
def listar_livros():
    """Lista todos os livros cadastrados na biblioteca."""
    # lista vazia conta como "falso", então "not biblioteca" significa "sem livros"
    if not biblioteca:
        print("\nNenhum livro cadastrado ainda.\n")
        return

    print("\nLista de livros cadastrados:")
    # enumerate numera os livros, começando do 1 (start=1)
    for i, livro in enumerate(biblioteca, start=1):
        print(f"{i}. {livro['titulo']} | Autor: {livro['autor']} | Gênero: {livro['genero']} | Quantidade: {livro['quantidade']}")
    print()


# Função 3: Pesquisar livro
def pesquisar_livro():
    """Permite pesquisar livros pelo título, autor ou gênero."""
    if not biblioteca:
        print("\nNão há livros cadastrados.\n")
        return

    print("\nPesquisar por:")
    print("1. Título")
    print("2. Autor")
    print("3. Gênero")
    opcao = input("Escolha o modo de pesquisa: ")

    # liga o número escolhido à chave do dicionário do livro
    campos = {"1": "titulo", "2": "autor", "3": "genero"}

    # se a opção não está no dicionário, avisa e volta ao menu
    if opcao not in campos:
        print("Opção inválida.\n")
        return

    campo = campos[opcao]
    termo = input("Digite o que você procura: ").strip().lower()

    resultados = []
    for livro in biblioteca:
        # "termo in texto" verifica se o termo aparece dentro do texto
        # lower() deixa tudo em minúsculas, assim a busca ignora maiúsculas
        if termo in livro[campo].lower():
            resultados.append(livro)

    if resultados:
        print("\nResultados encontrados:")
        for livro in resultados:
            print(f"- {livro['titulo']} ({livro['autor']}, {livro['genero']}) | Quantidade: {livro['quantidade']}")
        print()
    else:
        print("\nNenhum livro encontrado.\n")


# Função 4: Gerar gráfico
def gerar_grafico():
    """Gera um gráfico de barras mostrando a quantidade de livros por gênero."""
    if not biblioteca:
        print("\nNão há livros cadastrados para gerar gráfico.\n")
        return

    # Conta os livros por gênero.
    # generos.get(genero, 0) devolve o total já guardado, ou 0 se o gênero é novo
    generos = {}
    for livro in biblioteca:
        genero = livro["genero"]
        generos[genero] = generos.get(genero, 0) + livro["quantidade"]

    # Dados para o gráfico: nomes no eixo x e quantidades no eixo y
    nomes_generos = list(generos.keys())
    quantidades = list(generos.values())

    # Cria o gráfico de barras
    plt.bar(nomes_generos, quantidades, color="skyblue")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de livros")
    plt.title("Quantidade de livros por gênero")
    plt.xticks(rotation=45, ha="right")  # inclina os nomes para não ficarem sobrepostos
    plt.tight_layout()  # ajusta as margens para nada ser cortado
    plt.show()


# Função Menu Principal
def menu():
    """Exibe o menu de opções da biblioteca virtual."""
    # o while True repete o menu até o usuário escolher sair (break)
    while True:
        print("==== Biblioteca Virtual ====")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Pesquisar livro")
        print("4. Gerar gráfico por gênero")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            pesquisar_livro()
        elif opcao == "4":
            gerar_grafico()
        elif opcao == "5":
            print("Encerrando a biblioteca virtual. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# Execução do programa
menu()
