# Bot Gerenciador-de-Tarefas

## Breve descrição do projeto

- Programa Python permite ao usuário gerenciar uma lista de tarefas diretamente no terminal e armazenadas em um banco de dados(SQLITE)

## Funcionalidades

1. Menu de opções:
   - Ao inicializar o programa, será exibido um menu de opções com as escolhas.
2. Adicionar Tarefas:
   - Permite ao usuário adicionar uma nova tarefa com uma descrição.
3. Visualizar Tarefas:
   - Exibe todas as tarefas, indicando quais estão concluídas e quais ainda estão pendentes.
4. Marcar Tarefas como Concluídas:
   - Permite ao usuário marcar uma tarefa específica como concluída.
5. Remover Tarefas:
   - Permite ao usuário remover uma tarefa específica da lista.
6. Salvar e Carregar Tarefas:
   - Salvar a lista de tarefas em um arquivo para que elas possam ser carregadas na próxima execução do programa.
7. Ter a Persistência de dados
   - Todos os dados que foram inseridos ou modificados pelo usuário devem serão persistidos (ou seja, serão armazenados em algum local que não irá sumir após o programa fechar)

## Tecnologias

  - `sqlite3` -> Armazenar os arquivos
  - `rich` -> Para personalização do terminal
