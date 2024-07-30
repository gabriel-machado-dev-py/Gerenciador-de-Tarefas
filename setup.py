import sys
from cx_Freeze import setup, Executable 

files = ["README.md"]

# Executavel sem termina
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
    
configuracao = Executable(
  # Script onde esta a automacao
  script='app.py',
  # icone
  icon='task_list.ico'
)

# Configurar o executavel
setup(
    name='Bot Gereciador de Tarefas',
    version='1.0',
    description='Este é um bot gerenciador de tarefas',
    author='Gabriel Machado',
    options={
        'build_exe': {
            'include_files': files,
            'include_msvcr': True,
        }
    },
    executables=[configuracao]
)