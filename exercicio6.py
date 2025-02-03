
def eh_palindromo():
    print("Digite a palavra para verificar se é um palíndromo: ")
    palavra = input()
    palavra_ao_contrario = palavra[::-1]
    print(f"A palavra {palavra} ao contrário é {palavra_ao_contrario}")
    if palavra == palavra_ao_contrario:
        print("Ela é um palíndromo!")
eh_palindromo()
while True:
    print("Você quer continuar o programa?")
    condicao = input("Digite [S] para continuar ou [N] para sair do programa:")
    if condicao.upper() == "S":
        eh_palindromo()
    elif condicao.upper() == "N":
        break
    else:
        print("Opção inválida! digite 'S' ou 'N'.")