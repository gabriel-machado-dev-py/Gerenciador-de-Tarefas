import os
from tqdm import tqdm
from time import sleep
from pprint import pprint
# Breve descrição do projeto:
# Crie um programa em Python que permita ao usuário gerenciar uma lista de tarefas
# diretamente no terminal.
# O programa deve permitir adicionar, visualizar, marcar como concluídas e remover tarefas.
# Para que as tarefas não sejam perdidas de um dia para o outro, todos dados devem ser salvos
# em um banco de dados.
# O programa deve ser entregue como um executável.
# ○ Permitir ao usuário remover uma tarefa específica da lista.
# 6. Salvar e Carregar Tarefas:
# ○ Salvar a lista de tarefas em um arquivo para que elas possam ser carregadas na
# próxima execução do programa.
# 7. Ter a Persistência de dados
# ○ Todos os dados que foram inseridos ou modificados pelo usuário devem ser
# persistidos(ou seja, devem ser armazenados em algum local que não irá sumir
# após o programa fechar)

# Simulate a loading bar
print("Carregando programa:")
for _ in tqdm(range(100), desc="Loading", ncols=75):
    sleep(0.05)


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

print(CYAN + BOLD + r'''
                                                          _____                         
                    _|_|_|      _|__     _        _      |     |   \     /
                    _|    _|    _|  |    |        |      |      |   \   /
                    _|    _|    _|__      |_    _|       |  ___|     \_/
                    _|    _|    _|         |    |        |            |
                    _|_|_|      -|__|       |__|       .  |           |  
                                                                              
                                                                           
                           Programa Gerenciamento de Tarefas 
''' + RESET)

task_dict = {}

# Função para adicionar tarefas
def add_task(task_dict):
    task_id = len(task_dict) + 1
    task = input("Digite a tarefa que deseja adicionar: ")
    description = input("Digite a descrição da tarefa: ")
    
    task_dict[task_id] = {"Tarefa": task, "descrição": description, "status": "Pendente"}
    
    print(GREEN + f"Tarefa '{task}' adicionada com sucesso!" + RESET)
    print(BLUE + "Descrição da tarefa: " + description + RESET)

    return task_dict
 
# Função para visualizar tarefas
def view_task(task_dict):
    print(CYAN + BOLD + "Tarefas:" + RESET)
    if len(task_dict) == 0:
        print(RED + "Nenhuma tarefa adicionada!" + RESET)
        return task_dict
      
    for task_id, task in task_dict.items():
        print(f"{task_id} - {task['Tarefa']}: {task['descrição']}")
    print("\n")
    
    print(CYAN + BOLD + "Tarefas Concluídas:" + RESET)
    for task_id, task in task_dict.items():
        if task.get("status") == "Concluída":
            print(f"{task_id} - {task['Tarefa']}: {task['descrição']}")
    print("\n")
    
    print(CYAN + BOLD + "Tarefas Pendentes:" + RESET)
    for task_id, task in task_dict.items():
        if task["status"] != "Concluída":
            print(f"{task_id} - {task['Tarefa']}: {task['descrição']}")
    print("\n")
    
    
    return task
  
# Função para marcar tarefas como concluídas 
def mark_task_completed(task_dict):
  
    if len(task_dict) == 0:
      print(RED + "Nenhuma tarefa adicionada!" + RESET)
    else:  
      view_task(task_dict)
      task_id = int(input("Digite o ID da tarefa que deseja marcar como concluída: "))
      task_dict[task_id]["status"] = "Concluída"
      
      print(GREEN + f"Tarefa '{task_dict[task_id]['Tarefa']}' marcada como concluída!" + RESET)
    
    return task_dict
  
# Função para marcar tarefas como pendentes
def mark_task_pending(task_dict):
    
    if len(task_dict) == 0:
      print(RED + "Nenhuma tarefa adicionada!" + RESET)
    else:
      view_task(task_dict)
      task_id = int(input("Digite o ID da tarefa que deseja marcar como pendente: "))
      task_dict[task_id]["status"] = "Pendente"
      
      print(YELLOW + f"Tarefa '{task_dict[task_id]['Tarefa']}' marcada como pendente!" + RESET)
    
    return task_dict

while True:
    # 1.Menu de opções
    print(CYAN + BOLD + "Menu de Opções:" + RESET)
    print("1 - Adicionar Tarefa")
    print("2 - Visualizar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Marcar Tarefa como Pendente")
    print("5 - Sair")
    
    option = input("Digite a opção desejada: ")
    
    if option == "1":
        task_dict = add_task(task_dict)
    elif option == "2":
        view_task(task_dict)
    elif option == "3":
        task_dict = mark_task_completed(task_dict)
    elif option == "4":
        task_dict = mark_task_pending(task_dict)
    elif option == "5":
        break
    else:
        print(RED + "Opção inválida! Por favor, digite uma opção válida." + RESET)
    
    print("\n")

