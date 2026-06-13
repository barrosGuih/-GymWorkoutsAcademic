from rich import print
from rich.panel import Panel

treinos = []

def adicionar_treino():
    data = input("Data (dd/mm/aaaa): ")
    exercicio = input("Nome do exercício: ")
    series = int(input("Número de séries: "))
    repeticoes = int(input("Número de repetições: "))

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

adicionar_treino()


# Treinos de Academia: O sistema deve manter o registro dos exercícios de um dado aluno.
# Deve registrar data,
# nome/descrição do
# exercício, 
# número de repetições e séries.
