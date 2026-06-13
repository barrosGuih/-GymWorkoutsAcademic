
from rich.panel import Panel
from rich import print
from rich.align import Align

aluno = input("Digite o primeiro nome do aluno: ")

print(Panel(Align.center(f"[white]Seja bem-vindo, {aluno}![/white]"),
        width=35,
        border_style="white",
        title="[bold blue]Academia"))

print(Panel(Align.center("""
 [bold blue][1] - [white]Adicionar treino
 [bold blue][2] - [white]Listar treinos
 [bold blue][3] - [white]Exibir treino
 [bold blue][4] - [white]Exercícios do mês
 [bold blue][0] - [white]Sair """),
        width=35,
        title="[bold blue]Menu Principal")) 

# O menu deverá dispor, pelo menos, das seguintes opções: 
# Adicionar treino (onde registra cada exercício),
# Listar treinos (data e número de exercícios),
# Exibir treino (recebe data e mostra os exercícios de um dado dia),
#  Listar exercícios no mês (lista os exercícios, realizados no mês, sem repetições).