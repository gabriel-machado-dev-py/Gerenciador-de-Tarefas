from tqdm import tqdm
import os
# from rich import print
from rich.table import Table
from rich.console import Console
from time import sleep
import sqlite3

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Simulate a loading bar
print(f"{GREEN}Carregando programa...{RESET}")
print(f"{YELLOW + BOLD}Aguarde!{RESET}\n")
sleep(1.5)

for _ in tqdm(range(100), desc="Carregando", ncols=75):
    sleep(0.03)

print(CYAN + BOLD + r'''
                                                          _____                         
                    _|_|_|      _|__     _        _      |     |   \     /
                    _|    _|    _|  |    |        |      |      |   \   /
                    _|    _|    _|__      |_    _|       |  ___|     \_/
                    _|    _|    _|         |    |        |            |
                    _|_|_|      -|__|       |__|       .  |           |  
                                                                              
                                                                           
                           Programa Gerenciador de Tarefas 
''' + RESET)

print(CYAN + 'A programação é uma arte, assim como a pintura ou a escultura, que exige inspiração e criatividade para resolver problemas.' + RESET + '\n') 

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    tarefa TEXT NOT NULL,
    descricao TEXT NOT NULL,
    status TEXT NOT NULL
);
''')

# Função para adicionar tarefas
def insert_task(task, description, status):
    cursor.execute(f'''
    INSERT INTO tasks (tarefa, descricao, status)
    VALUES (?, ?, ?)
    ''', (task, description, status))
    conn.commit()
    
    print(GREEN + f"Tarefa '{task}' adicionada com sucesso!" + RESET)
    print(BLUE + "Descrição da tarefa: " + description + RESET)
    
# Função para visualizar tarefas
def view_tasks():
    cursor.execute('''
    SELECT * FROM tasks
    ''')
    tasks = cursor.fetchall()
    
    table = Table(title="Tarefas Cadastradas")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Tarefa", style="magenta")
    table.add_column("Descrição", style="green")
    table.add_column("Status", style="blue")
    
    for task in tasks:
        table.add_row(str(task[0]), task[1], task[2], task[3])
    
    console = Console()
    console.print(table)
    
    return tasks

# Função para marcar tarefa como concluída
def mark_task_as_done(task_id):
    cursor.execute(f'''
    UPDATE tasks
    SET status = 'Concluída'
    WHERE id = ?
    ''', (task_id,))
    conn.commit()
    
    print(GREEN + f"Tarefa ID {task_id} marcada como concluída!" + RESET)
    
# Função para remover tarefa
def remove_task(task_id):
    cursor.execute(f'''
    DELETE FROM tasks
    WHERE id = ?
    ''', (task_id,))
    conn.commit()
    
    print(RED + f"Tarefa ID {task_id} removida com sucesso!" + RESET)
    

def main_menu():
    while True:
        # 1.Menu de opções
        print(CYAN + BOLD + "Menu de Opções:" + RESET)
        print(GREEN + "1 - Adicionar Tarefa" + RESET)
        print(GREEN + "2 - Visualizar Tarefas" + RESET)
        print(GREEN + "3 - Marcar Tarefa como Concluída" + RESET)
        print(GREEN + "4 - Remover Tarefa" + RESET)
        print(RED + "5 - Sair" + RESET)
        
        option = input("Digite a opção desejada: ")
        
        if option == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            
            task = input("Digite a tarefa: ")
            description = input("Digite a descrição da tarefa: ")
            status = "Pendente"
            
            insert_task(task, description, status)
        elif option == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            view_tasks()
        elif option == "3":
            tasks = view_tasks()
            
            if len(tasks) == 0:
                print(YELLOW + "Não há tarefas cadastradas!" + RESET)
                continue
            
            task_id = input("Digite o ID da tarefa que deseja marcar como concluída: ")
            mark_task_as_done(task_id)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            
            view_tasks()
        elif option == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            
            tasks = view_tasks()
            if len(tasks) == 0:
                print(YELLOW + "Não há tarefas cadastradas!" + RESET)
                continue
            
            task_id = input("Digite o ID da tarefa que deseja remover: ")
            remove_task(task_id)
            view_tasks()
        elif option == "5":
            print(YELLOW + "Saindo do programa..." + RESET)
            print(YELLOW + "Até mais!" + RESET)
            sleep(2)
            break
        else:
            print(RED + "Opção inválida!" + RESET)
        print("\n")

if __name__ == "__main__":
    try:
        main_menu()
    finally:
        conn.close()