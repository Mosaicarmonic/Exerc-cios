import time
dicionario = {}
def exibir_menu():
    print("\nEscolha uma opção abaixo:")
    print("1. Adicionar palavra e significado")
    print("2. Consultar significado")
    print("3. Exibir todas as palavras e significados")
    print("4. Remover uma palavra e significado")
    print("5. sair")

def adicionar_palavra_e_significado():
    palavra = input("Digite a palavra que deseja adicionar:").strip
    significado = input("Digite o significado da palavra: ").strip
    if palavra in dicionario:
        print("A palavra já existe, deseja atualizar o significado? s/n")
        confirmar = input().lower
        if confirmar == 's':
            dicionario[palavra] = significado
            print("Significado atualizado!")
        else:
            print("A operação foi cancelada!")
    else:
        dicionario[palavra] = significado
        print("Palavra e significado adicionados com sucesso!")

def consultar_significado():
    palavra = input("Digite a palavra que queira acessar seu significado: ")
    if palavra in dicionario:
        print(f"O significado de {palavra} é: \n{dicionario[palavra]}")
    else:
        print("Palavra não encontrada.")

def exibir_tudo():
    if not dicionario:
        print("Dicionário vazio.")
    else:
        for palavra, significado in dicionario.items():
            print(f"{palavra}: {significado}")

def remover_palavra():
    palavra = input("Digite a palavra que deseja remover:")
    if palavra in dicionario:
        del dicionario[palavra]
        print("Palavra removida com sucesso.")
    else:
        print("Palavra não encontrada no dicionário.")

def main():
    while True:
        exibir_menu()
        opcao = input()
        match opcao:
            case "1":
                adicionar_palavra_e_significado()
            case "2":
                consultar_significado()
            case "3":
                exibir_tudo()
            case "4":
                remover_palavra()
            case "5":
                print("saindo...")
                time.sleep(2)
                break
            case _:
                print("Digite uma opção válida!")

if __name__ == "__main__":
    main()