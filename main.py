from rich import print
from rich.panel import Panel
from rich.align import Align

treinos = []


def menu_principal():

    print(Panel(Align.center("""
 [bold blue][1] - [white]Adicionar treino
 [bold blue][2] - [white]Listar treinos
 [bold blue][3] - [white]Exibir treino
 [bold blue][4] - [white]Exercícios do mês
 [bold blue][0] - [white]Sair """),
        width=35,
        title="[bold blue]Menu Principal")) 
    
    option = (input("Escolha uma das opções: "))

    def validacao():   #TESTA SE A ENTRADA SERÁ SOMENTE NUMEROS INTEIROS.
       while True:
            try:
                print("[red]Valor invalido, tente novamente")
                option = int(input("Escolha uma das opções: "))

            except ValueError:
                print("[red]Valor invalido, tente novamente")

                if 4 < option < 0:
                    print("[red]Valor invalido, tente novamente")
                    menu_principal()
                    option = int(input("Escolha uma das opções: "))

            return option
       
    validacao()

    if option == 1:
        adicionar_treino()
    if option == 2:
        listar_treinos()
    if option == 3:
        exibir_treino()
    if option == 4:
        listar_exercicios_mes()


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


aluno = input("Digite o primeiro nome do aluno: ").strip()

if not aluno.isalpha():  #Verifica se foi digitado número, se sim pede o nome novamente.
    print("[red]Nome invalido, tente novamente")
    aluno = input("Digite o primeiro nome do aluno: ").strip()

print(Panel(Align.center(f"[white]Seja bem-vindo, {aluno.capitalize()}![/white]"),
        width=35,
        border_style="white",
        title="[bold blue]Academia"))

menu_principal()
