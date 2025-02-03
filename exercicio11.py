import math
def trigonometria():
    while True:
        try:
            angulo = math.degrees(float(input("Digite o valor do ângulo:")))
            break
        except ValueError:
            print("Digite um número válido!")
    print(f"O seno, cosseno e tangente do ângulo {angulo}°, são respectivamente, {math.sin(angulo)}, {math.cos(angulo)} e {math.tan(angulo)}")
trigonometria()
while True:
    print("Você deseja fazer mais uma operação? (s/n)")
    opcao = input
    if opcao.lower() == "s":
        trigonometria()
    elif opcao.lower() == "n":
        break
    else:
        print("Digite uma opção válida!")