pessoas = {
    "Alice": 21,
    "Bruna": 18,
    "Gustavo": 17,
    "Carlos": 19
}

print("As idades das pessoas presente no banco de dados são: ")

for i in pessoas:
    print(f"{i}: {pessoas[i]} anos")

nome_remover = "Gustavo"

if nome_remover in pessoas:
    pessoas.pop(nome_remover)
    print(f"{nome_remover} foi removido do dicionário.")
else:
    print(f"{nome_remover} não foi encontrado no dicionário.")

print("Dicionário atualizado: ", pessoas)