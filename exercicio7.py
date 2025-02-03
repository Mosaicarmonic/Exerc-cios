lista = [10, 20, 30, 40, 50]
lista_invertida = lista[::-1]
lista_nova = lista
lista_nova[2] = 100

print(f"A lista {lista} invertida é {lista_invertida}!")
print(f"A soma dos elementos da lista é de {sum(lista)}!")
print(f"A lista {lista} quando o terceiro elemento \ndela é substituido por 100 fica {lista_nova}!")