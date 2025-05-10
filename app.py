import os 

restaurantes = [
    {"nome": "Restaurante 01", "categoria": "Pizza", "ativo": False},
    {"nome": "Restaurante 02", "categoria": "Sushi", "ativo": True},
    {"nome": "Restaurante 03", "categoria": "Churrasco", "ativo": False}
]

def exibir_nome_do_programa():
    """
    Função para exibir o nome do programa na tela.
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    """
    Função para exibir as opções disponíveis no menu principal.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar o estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    """
    Função para finalizar o aplicativo. O usuário deve pressionar 'Enter' para sair.
    """
    subtitulo("Finalizando o app")

def voltar_main():
    """
    Função para voltar ao menu principal. O usuário deve pressionar 'Enter' para voltar.
    """
    input("\nPressione 'Enter' para voltar ao menu principal ")
    main()

def opcao_invalida():
    """
    Função para exibir uma mensagem de opção inválida. 
    O usuário deve pressionar 'Enter' para voltar ao menu principal. 
    """
    print("Opcão inválida!\n")
    voltar_main()

def subtitulo(text):
    """
    Função para exibir um subtítulo na tela. O subtítulo é exibido com
    uma linha de asteriscos acima e abaixo do texto."""
    os.system('cls')
    linha = "*"*(len(text))
    print(linha)
    print(f"{text}")
    print(linha)

def cadastrar_restaurante():
    """
    Função para cadastrar um restaurante. O usuário deve informar o 
    nome e a categoria do restaurante. O restaurante é cadastrado como
    desativado por padrão.

    Inputs:
    - nome_restaurante: str, nome do restaurante a ser cadastrado.
    - categoria_restaurante: str, categoria do restaurante a ser cadastrado.

    Outputs:
    - dados_restaurante: dict, dicionário com os dados do restaurante.
    """
    subtitulo("Cadastrar restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input("Digite o nome da categoria do restaurante: ")
    dados_restaurante = {
        "nome": nome_restaurante,
        "categoria": categoria_restaurante,
        "ativo": False
    }
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!\n")
    voltar_main()

def listar_restaurantes():
    """
    Função para listar os restaurantes cadastrados. A lista é exibida com o nome,
    categoria e status do restaurante (ativado ou desativado).

    Inputs:
    - restaurantes: list, lista de dicionários com os dados dos restaurantes.

    Outputs:
    - None, apenas exibe a lista de restaurantes cadastrados.
    """
    subtitulo("Listar restaurantes")
    print(f"{"Nome do restaurante:".ljust(20)}  |  {"Categoria:".ljust(20)}  |  {"Status:".ljust(20)}")
    for r in restaurantes:
        nome_restaurante = r["nome"]
        categoria_restaurante = r["categoria"]
        ativo_restaurante = "Ativado" if r["ativo"] else "Desativado"
        print(f"{nome_restaurante.ljust(20)}  |  {categoria_restaurante.ljust(20)}  |  {ativo_restaurante.ljust(20)}")
    voltar_main()

def estado_restaurante():
    """
    Função para alterar o estado do restaurante. O usuário deve informar o 
    nome do restaurante que deseja alterar o estado. O estado do restaurante é
    alterado de ativado para desativado ou vice-versa.

    Inputs:
    - nome_restaurante: str, nome do restaurante a ser alterado.

    Outputs:
    - None, apenas altera o estado do restaurante e exibe uma mensagem de sucesso.
    """
    subtitulo("Alterar o estado do restaurante")
    print("Lista de restaurantes: ")
    for r in restaurantes:
        print(f"-> {r["nome"]}")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for r in restaurantes:
        if nome_restaurante == r["nome"]:
            restaurante_encontrado = True
            r["ativo"] = not r["ativo"]
            if r["ativo"]:
                print(f"O restaurante {r["nome"]} foi ativado com sucesso!")
            else:
                print(f"O restaurante {r['nome']} foi desativado com sucesso!")
    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} não foi encontrado!")
    voltar_main()

def escolher_opcao():
    """
    Função para escolher a opção do menu principal. O usuário deve informar
    o número da opção desejada. A função verifica se a opção é válida e executa
    a função correspondente. Se a opção for inválida, exibe uma mensagem de erro."""
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """Função principal do aplicativo. Limpa a tela, exibe o nome do programa,
    exibe as opções do menu principal e chama a função para escolher a opção."""
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
