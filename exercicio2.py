print("Digite dois números:")

while True:
    try:
        numero_1 = int(input())
        numero_2 = int(input())
        break
    except ValueError:
        print("Digite números válidos!")

divisao = None

try:
    divisao = numero_1 / numero_2
except ZeroDivisionError:
    print("Não foi possível dividir por 0")

print(f"Soma: {numero_1 + numero_2}")
print(f"Subtração: {numero_1 - numero_2}")
print(f"Multiplicação: {numero_1 * numero_2}")
if divisao is not None:
    print(f"Divisão: {divisao}")
else:
    print("Não foi calculado devido a um erro.")
input()