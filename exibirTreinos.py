from rich.prompt import Prompt
from rich.panel import Panel
from rich import print
import time

def exibir_treino(treinos):
    if not treinos:
        print(Panel.fit("[yellow]Nenhum treino cadastrado!"))
        return

    data_busca = Prompt.ask("[white]Digite o dia(dd mm aaaa) que voce quer saber o treino[/white]").strip()
    try:
        dia,mes,ano = data_busca.split()
    except ValueError:
        print("[red]Formato inválido! Use dd mm aaaa[/red]")
        time.sleep(1)
        return
    
    dia = dia.zfill(2)
    mes = mes.zfill(2)
    data_busca = dia+" "+mes+" "+ano
        
    if data_busca in treinos:
        for exercicios in treinos[data_busca]:
            print(Panel.fit(f" [bold blue]- [white]{exercicios['nome']} ({exercicios['series']}x{exercicios['repeticoes']})",
                        title=f"[bold blue]Data: [white]{data_busca.replace(" ","/")}"))
            time.sleep(0.5)
    else:
        print("[yellow]Nenhum treino encontrado nessa data")
        time.sleep(1)
