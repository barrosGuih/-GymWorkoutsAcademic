from rich.prompt import Prompt
from rich.panel import Panel
from rich import print

def listar_exercicios_mes(treinos):
    if not treinos:
        print("[yellow]Nenhum treino cadastrado!")
        return
    
    mes = Prompt.ask("[white]Selecione o mes (1-12)[/white]").strip()

    if len(mes) == 1:  ## tratar erros de entradas incorretas
        mes = "0" + mes
    encontrou = False
    for data in treinos:
        mesData = data[3:5] ## se o cara colocar 12/05/2026  queremos o index 3 e 4 no caso 05
        if mesData == mes:
            encontrou = True
                  
            for exercicios in treinos[data]:
                print(Panel.fit(f" [bold blue]- [white]{exercicios['nome']} ({exercicios['series']}x{exercicios['repeticoes']})",
                        title=f"[bold blue]Data: [white]{data.replace(" ","/")}"))
    if not encontrou:
        print(f"[red]Nenhum treino encontrado para o mês {mes}.")
