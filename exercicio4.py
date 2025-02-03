import time
lista = []
print("Números pares de 1 a 50: ", end="")
for n in range(1, 51):
    if n%2 == 0 and n!=50:
        print(f"{n}, ", end="")
    elif n == 50:
        print(f"{n}.")
    else:
        lista.append(n)

soma_impares = sum(lista)

print(f"A soma dos números impares de 1 a 50 é de: {soma_impares}")

while True:
    time.sleep(5)