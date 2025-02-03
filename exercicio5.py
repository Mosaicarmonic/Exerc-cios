def numeros():
    print("Digite dois números para calcular área de um triangulo:")
    while True:
        try:
            altura = float(input("Altura: "))
            base = float(input("Base: "))
            if altura > 0 and base > 0:
                break
            else:
                print("Digite dois números positivos: ")
        except ValueError:
            print("Digite dois números válidos!")
    return altura, base

def area_triangulo():
    altura, base = numeros()
    print(f"A área do triângulo é de {(altura * base)/2}")

while True:
    print("Você quer começar o programa?: \n [S] para sim \n [N] para não")
    valor = input()
    if valor.upper() == "S":
        area_triangulo()
    elif valor.upper() == "N":
        break
    else:
        print("Opção inválida! Digite 'S' para sim ou 'N' para não.")