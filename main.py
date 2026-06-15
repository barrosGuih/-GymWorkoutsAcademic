# ==================================================
# IMPORTS
# ==================================================
from rich.prompt import IntPrompt
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from rich import print
import time
from SavedData import carregar_txt
from adicionarTreino import adicionar_treino
from exibirTreinos import exibir_treino
from listarExerciciosMes import listar_exercicios_mes
from listarTreinos import listar_treinos

treinos = {}# Dicionário principal
console = Console() # transforma o console em função para facilitar e melhorar a exibição no terminal

def validacao():                
    while True:
        try:
            option = IntPrompt.ask("[yellow]Escolha uma das opções")

            if 0 <= option <= 4: # limita option aos nuemros da tabela
                return option
            else:
                print(Panel.fit("[red]Valor invalido, tente novamente"))
                
        except ValueError:
            print(Panel.fit("[red]Valor invalido, tente novamente"))
def menu_principal():
  
 while True:

    print(Panel(Align.center("""
 [bold blue][1] - [white]Adicionar treino
 [bold blue][2] - [white]Listar treinos
 [bold blue][3] - [white]Exibir treino
 [bold blue][4] - [white]Exercícios do mês
 [bold blue][0] - [white]Sair """),
        width=35,
        title="[bold blue]Menu Principal")) 
    time.sleep(1)

    option = validacao()

    if option == 1:
        time.sleep(0.5)
        adicionar_treino(treinos, aluno)
    elif option == 2:
        listar_treinos(treinos)
    elif option == 3:
        exibir_treino(treinos)
    elif option == 4:
        time.sleep(0.5)
        listar_exercicios_mes(treinos)
    elif option == 0:
        time.sleep(0.5)
        print("[yellow]Saindo do sistema...")
        break

while True:                      
    aluno = Prompt.ask("[white]Digite o primeiro nome do aluno[/white]").strip()

    if aluno.isalpha():  #Verifica se foi digitado número, se sim pede o nome novamente.
       break
    print("[red]Nome invalido, tente novamente")

treinos = carregar_txt(aluno) 

print(Panel(Align.center(f"[white]Seja bem-vindo a [yellow]AGE FITNESS[/yellow], {aluno.capitalize()}![/white]"),
        width=35,
        border_style="white",
        title="[bold blue]Academia AGE Fitness"))

# ==================================================
# INICIO DO DESASTRE
# ==================================================

menu_principal()