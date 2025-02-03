import time
import os
def menu():
    while True:
        print("Qual opção você deseja fazer? \n [1] Ver todas as tarefas pendentes.\n [2] Adicionar nova tarefa. \n [3] Finalizar tarefa. \n [4] Sair do programa.")
        opcao = input()
        match opcao:
            case '1':
                ver_tarefas_pendentes()
            case '2':
                adicionar_tarefa()
            case '3':
                finalizar_tarefa()
            case '4':
                print("Saindo...")
                time.sleep(3)
                break
            case _:
                print("Digite uma opção válida!")

def ver_tarefas_pendentes():
    with open('Tarefas.txt', 'r') as tarefas:
        for linha in tarefas:
            print(linha, end='')
    print()  

def adicionar_tarefa():
    nova_tarefa = input("Digite a nova tarefa que queira adicionar: ")
    with open('Tarefas.txt', 'r') as tarefas:
        linhas = tarefas.readlines()
    if nova_tarefa.strip() not in [linha.strip() for linha in linhas]:
        with open('Tarefas.txt', 'a') as tarefas:
            tarefas.write(nova_tarefa.strip() + "\n")
        print("Tarefa adicionada com sucesso!")
    else:
        print("A tarefa já existe!")

def finalizar_tarefa():
    tarefa_excluida = input("Digite a tarefa que já finalizou: ")
    with open('Tarefas.txt', 'r') as tarefas:
        linhas = tarefas.readlines()
    linhas_filtradas = [linha for linha in linhas if tarefa_excluida.strip() not in linha.strip()]
    with open('Tarefas.txt', 'w') as tarefas:
        tarefas.writelines(linhas_filtradas)
    print("Tarefa eliminada!")
Lista = "Tarefas.txt"
if not os.path.exists(Lista):
    with open(Lista, 'w') as arquivo:
        arquivo.write("**Lista de tarefas**\n")
menu()