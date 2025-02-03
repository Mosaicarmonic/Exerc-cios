print("Digite um número natural válido de 1 a 100:")

while True:
    try:
        numero = int(input())
        if 1 <= numero <= 100:
            break
        else:
            print("Por favor, digite um número natural válido de 1 a 100!")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

divisores = []

for n in range(1, numero+1):
    if numero % n == 0:
        divisores.append(n)

print(f"Os divisores de {numero} são: {', '.join(map(str, divisores))}.")

if len(divisores) == 2:
    print(f"O número {numero} é primo!")
        
input()