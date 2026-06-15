from rich.panel import Panel
from rich import print

def listar_treinos(treinos):
    if not treinos:
        print("[yellow]Nenhum treino cadastrado!")
        return
    
    print(Panel.fit("[bold blue]Treinos cadastrados:[bold blue]"))

    for data in treinos:
        qnt_execicios = len(treinos[data])
        
        print(Panel.fit(f"[bold blue]Data: [white]{data.replace(" ","/")} [white]([bold blue]{qnt_execicios}[white]: exercício(s))"))