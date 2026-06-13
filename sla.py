from rich import print
from rich.panel import Panel
from rich.align import Align

treinos = []

def validacao():
    """Garante que a entrada seja um número entre 0 e 4."""
    while True:
        try:
            # Tenta converter a entrada para inteiro
            opcao = int(input("Escolha uma das opções: "))
            
            # Verifica se o número está no intervalo correto
            if 0 <= opcao <= 4:
                return opcao
            else:
                print("[red]Opção inválida! Escolha um número entre 0 e 4.")
        except ValueError:
            # Se o usuário digitar letras ou símbolos
            print("[red]Erro: Digite apenas números inteiros.")

def menu_principal():
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
        adicionar_treino()
    elif option == 2:
        listar_treinos()
    elif option == 3:
        exibir_treino()
    elif option == 4:
        listar_exercicios_mes()
    elif option == 0:
        print("[yellow]Saindo do programa...")
        return # Encerra a função

def adicionar_treino():
    try:
        data = input("Data (dd/mm/aaaa): ").strip()
        exercicio = input("Nome do exercício: ").strip()
        # O .strip() deve vir antes de converter para int
        series = int(input("Número de séries: ").strip())
        repeticoes = int(input("Número de repetições: ").strip())

        treino = {
            "data": data,
            "exercicio": exercicio,
            "series": series,
            "repeticoes": repeticoes
        }

        treinos.append(treino)  
        print(Panel.fit(f"[green]Treino cadastrado com sucesso!"))
        
        # Volta ao menu após cadastrar
        menu_principal()
        
    except ValueError:
        print("[red]Erro: Séries e repetições devem ser números inteiros.")
        adicionar_treino() # Tenta novamente se digitar errado

def listar_treinos():
    print("Listando treinos...") # Implemente aqui

def exibir_treino():
    print("Exibindo treino...") # Implemente aqui

def listar_exercicios_mes():
    print("Exercícios do mês...") # Implemente aqui

# --- INÍCIO DO PROGRAMA ---

# Melhorar a validação do nome usando um loop while
while True:
    aluno = input("Digite o primeiro nome do aluno: ").strip()
    if aluno.isalpha():
        break
    print("[red]Nome inválido, use apenas letras.")

print(Panel(Align.center(f"[white]Seja bem-vindo, {aluno.capitalize()}![/white]"),
        width=35,
        border_style="white",
        title="[bold blue]Academia"))

menu_principal()