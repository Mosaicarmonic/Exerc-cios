def contar_linhas_palavras_caracteres(nome_arquivo):
    while True:
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readline()
                num_linhas= len(linhas)
                num_palavras= sum(len(linha.split()) for linha in linhas)
                num_caracteres= sum(len(linha) for linha in linhas)
                print(f"Número de linhas: {num_linhas}")
                print(f"Número de palavras: {num_palavras}")
                print(f"Número de caracteres: {num_caracteres}")
                break
        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}.")
def iniciar():
    nome_arquivo = input("Digite o nome arquivo que deseja ler:")
    contar_linhas_palavras_caracteres(nome_arquivo)
iniciar()
while True:
    print("Você deseja fazer mais uma operação? (s/n)")
    opcao = input
    if opcao.lower() == "s":
        iniciar()
    elif opcao.lower() == "n":
        break
    else:
        print("Digite uma opção válida!")
