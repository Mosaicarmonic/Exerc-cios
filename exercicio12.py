import math
def calcular_raiz_da_soma_de_dois_quadrados():
    print("Digite dois números para calcular:")
    while True:
        try:
            x = float(input())
            y = float(input())
            break
        except ValueError:
            print("Digite números válidos!")
    print(f"O resultado da raiz da soma dos quadrados dos números fornecidos é de {math.sqrt(((x**2)+(y**2)))}!")
calcular_raiz_da_soma_de_dois_quadrados()
while True:
    print("Você deseja fazer mais uma operação? (s/n)")
    opcao = input
    if opcao.lower() == "s":
        calcular_raiz_da_soma_de_dois_quadrados()
    elif opcao.lower() == "n":
        break
    else:
        print("Digite uma opção válida!")