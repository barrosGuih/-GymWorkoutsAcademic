from rich import print
from rich.panel import Panel
from rich.align import Align

treinos = []

aluno = input("Digite o primeiro nome do aluno: ")

print(Panel(Align.center(f"[white]Seja bem-vindo, {aluno}![/white]"),
        width=35,
        border_style="white",
        title="[bold blue]Academia"))

def menu_principal():

    print(Panel(Align.center("""
 [bold blue][1] - [white]Adicionar treino
 [bold blue][2] - [white]Listar treinos
 [bold blue][3] - [white]Exibir treino
 [bold blue][4] - [white]Exercícios do mês
 [bold blue][0] - [white]Sair """),
        width=35,
        title="[bold blue]Menu Principal")) 

def adicionar_treino():
    data = input("Data (dd/mm/aaaa): ").strip()
    exercicio = input("Nome do exercício: ").strip()
    series = int(input("Número de séries: ")).strip()
    repeticoes = int(input("Número de repetições: ")).strip()

    treino = {
        "data": data,
        "exercicio": exercicio,
        "series": series,
        "repeticoes": repeticoes
    }

    treinos.append(treino)  

    print(Panel.fit(f" [green]Treino cadastrado com sucesso! "))

def listar_treinos():
    pass

def exibir_treino():
    pass

def listar_exercicios_mes():
    pass

def menu():
    pass

#adicionar_treino()


# Treinos de Academia: O sistema deve manter o registro dos exercícios de um dado aluno.
# Deve registrar data,
# nome/descrição do
# exercício, 
# número de repetições e séries.
