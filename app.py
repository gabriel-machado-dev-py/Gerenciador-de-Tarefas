from tqdm import tqdm
from time import sleep
import sqlite3

# Simulate a loading bar
# print("Carregando programa:")
# for _ in tqdm(range(100), desc="Loading", ncols=75):
#     sleep(0.05)


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

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa TEXT NOT NULL,
    descricao TEXT NOT NULL,
    status TEXT NOT NULL
);
''')

# Função para adicionar tarefas
def insert_task(task, description, status):
    cursor.execute(f'''
    INSERT INTO tasks (tarefa, descricao, status)
    VALUES ('{task}', '{description}', '{status}')
    ''')
    conn.commit()
    print(GREEN + f"Tarefa '{task}' adicionada com sucesso!" + RESET)
    print(BLUE + "Descrição da tarefa: " + description + RESET)
    
# Função para visualizar tarefas
def view_tasks():
    cursor.execute('''
    SELECT * FROM tasks
    ''')
    tasks = cursor.fetchall()
    print(CYAN + BOLD + "Tarefas Cadastradas:" + RESET)
    for task in tasks:
        print(f"ID: {task[0]} - Tarefa: {task[1]} - Descrição: {task[2]} - Status: {task[3]}")
    return tasks
# Função para marcar tarefa como concluída
def mark_task_as_done(task_id):
    cursor.execute(f'''
    UPDATE tasks
    SET status = 'Concluída'
    WHERE id = {task_id}
    ''')
    conn.commit()
    print(GREEN + f"Tarefa ID {task_id} marcada como concluída!" + RESET)
    
# Função para remover tarefa
def remove_task(task_id):
    cursor.execute(f'''
    DELETE FROM tasks
    WHERE id = {task_id}
    ''')
    conn.commit()
    print(RED + f"Tarefa ID {task_id} removida com sucesso!" + RESET)
    


while True:
    # 1.Menu de opções
    print(CYAN + BOLD + "Menu de Opções:" + RESET)
    print("1 - Adicionar Tarefa")
    print("2 - Visualizar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Remover Tarefa")
    print("5 - Sair")
    
    option = input("Digite a opção desejada: ")
    
    if option == "1":
        task = input("Digite a tarefa: ")
        description = input("Digite a descrição da tarefa: ")
        status = "Pendente"
        insert_task(task, description, status)
    elif option == "2":
        view_tasks()
    elif option == "3":
        tasks = view_tasks()
        if len(tasks) == 0:
            print(YELLOW + "Não há tarefas cadastradas!" + RESET)
            continue
        task_id = input("Digite o ID da tarefa que deseja marcar como concluída: ")
        mark_task_as_done(task_id)
    elif option == "4":
        tasks = view_tasks()
        if len(tasks) == 0:
            print(YELLOW + "Não há tarefas cadastradas!" + RESET)
            continue
        task_id = input("Digite o ID da tarefa que deseja remover: ")
        remove_task(task_id)
    elif option == "5":
        print(YELLOW + "Saindo do programa..." + RESET)
        break
    else:
        print(RED + "Opção inválida!" + RESET)
    print("\n")

