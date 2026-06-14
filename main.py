from rich import print
from rich.panel import Panel
from rich.align import Align
import time

treinos = {}

def validacao():   #TESTA SE A ENTRADA SERÁ SOMENTE NUMEROS INTEIROS.
    while True:
        try:
            option = int(input("Escolha uma das opções: "))
            if 0 <= option <= 4:
                return option
            else:
                print("[red]Valor invalido, tente novamente") 
        except ValueError:
            print("[red]Valor invalido, tente novamente")

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

    option = validacao()

    if option == 1:
        time.sleep(1)
        adicionar_treino()
    elif option == 2:
        time.sleep(1)
        listar_treinos()
    elif option == 3:
        time.sleep(1)
        exibir_treino()
    elif option == 4:
        time.sleep(1)
        listar_exercicios_mes()
    elif option == 0:
        print("[yellow]Saindo do sistema...")
        break

def adicionar_treino():
    data = input("Data (dd/mm/aaaa): ").strip()## colocar verificacao na data

    if not data:
        print("Erro: A data nao pode ser vazia")
        return
    
    if data not in treinos:
        treinos[data] = []
    
    while True:
        exercicio = input("Nome do exercício: ").strip()
        if not exercicio:
            print("Erro: o nome do exercicio nao pode ser vazia")
            continue

        try:
            series = int(input("Número de séries: "))
            repeticoes = int(input("Número de repetições: "))

            if series <= 0 or repeticoes <= 0:
                print("Erro: nao pode ser menor ou igual a 0")
                continue
        except ValueError:
            print("Digite so numeros inteiros validos")
            continue

        exercicio = {
        "nome": exercicio,
        "series": series,
        "repeticoes": repeticoes
        }

        treinos[data].append(exercicio)  
        print(Panel.fit(f"\n [green]Treino cadastrado com sucesso! \n"))

        loopOpcao = input(f"Deseja adicionar outro exercicio na mesma data ({data})? (S/N): ").format(data).strip().upper()
        if loopOpcao != "S":
            break

def listar_treinos():
    if not treinos:
        print("[yellow]Nenhum treino cadastrado!")
        return
    
    print("Treinos cadastrados:")

    for data in treinos: ## descrever...
        print(f"[bold]Data: {data}[/bold]")
    
    for info in treinos[data]:
        print(Panel.fit(f" - {info['nome']},  series: {info['series']}   repeticoes: {info['repeticoes']}"))

def exibir_treino():
    if not treinos:
        print("[yellow]Nenhum treino cadastrado!")
        return

    diaEscolhidoEncontrado = False

    diaEscolhido = input("Digite o dia(dd/mm/aaaa) que voce quer saber o treino: ")
    for data in treinos:
        DiaVerificado = data[0:]
        if DiaVerificado == diaEscolhido:
            diaEscolhidoEncontrado = True
            print(f"\n[bold blue]Data: {data}[/bold blue]")
            
            
            for exercicios in treinos[data]:
                print(f" - {exercicios['nome']} ({exercicios['series']}x{exercicios['repeticoes']})")
        else:
            print("[yellow]Nenhum treino encontrado nessa data")
            time.sleep(1)
            continue


def listar_exercicios_mes():
    if not treinos:
        print("[yellow]Nenhum treino cadastrado!")
        return
    
    mes = input("Selecione o mes (1-12): ").strip() ## tratar erros de entradas incorretas

    if len(mes) == 1:
        mes = "0" + mes
    
    encontrou = False

    for data in treinos:
        mesData = data[3:5] ## se o cara colocar 12/05/2026  queremos o index 3 e 4 no caso 05
        if mesData == mes:
            encontrou = True
            print(f"\n[bold blue]Data: {data}[/bold blue]")
            
            
            for exercicios in treinos[data]:
                print(f" - {exercicios['nome']} ({exercicios['series']}x{exercicios['repeticoes']})")

    if not encontrou:
        print(f"[red]Nenhum treino encontrado para o mês {mes}.")




while True:
    aluno = input("Digite o primeiro nome do aluno: ").strip()

    if aluno.isalpha():  #Verifica se foi digitado número, se sim pede o nome novamente.
       break
    print("[red]Nome invalido, tente novamente")

print(Panel(Align.center(f"[white]Seja bem-vindo, {aluno.capitalize()}![/white]"),
    width=35,
    border_style="white",
    title="[bold blue]Academia"))

menu_principal()