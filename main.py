from rich import print
from rich.panel import Panel
from rich.align import Align
import time
import os

# Nome do arquivo de texto
ARQUIVO = "treinos.txt"

def salvar_txt(dados):
    """Transforma o dicionário em linhas de texto e salva no arquivo."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for data, lista_exercicios in dados.items():
            for ex in lista_exercicios:
                # Salva no formato: data;nome;series;repeticoes
                linha = f"{data};{ex['nome']};{ex['series']};{ex['repeticoes']}\n"
                f.write(linha)

def carregar_txt():
    """Lê o arquivo TXT e reconstrói o dicionário 'treinos'."""
    dados_carregados = {}
    if not os.path.exists(ARQUIVO):
        return {}

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            # Remove o \n e separa os dados pelo ;
            partes = linha.strip().split(";")
            if len(partes) == 4:
                data = partes[0]
                nome = partes[1]
                series = int(partes[2])
                reps = int(partes[3])

                if data not in dados_carregados:
                    dados_carregados[data] = []
                
                dados_carregados[data].append({
                    "nome": nome,
                    "series": series,
                    "repeticoes": reps
                })
    return dados_carregados

# Inicializa o dicionário carregando do TXT
treinos = carregar_txt()

def validacao():
    while True:
        try:
            option = int(input("Escolha uma das opções: "))
            if 0 <= option <= 4:
                return option
            print("[red]Valor inválido, tente novamente") 
        except ValueError:
            print("[red]Valor inválido, tente novamente")

def menu_principal():
    while True:
        print(Panel(Align.center("""
 [bold blue][1] - [white]Adicionar treino
 [bold blue][2] - [white]Listar treinos
 [bold blue][3] - [white]Exibir treino
 [bold blue][4] - [white]Exercícios do mês
 [bold blue][0] - [white]Sair """),
            width=35, title="[bold blue]Menu Principal")) 

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
            print("[yellow]Saindo e salvando dados...")
            break

def adicionar_treino():
    data = input("Data (dd/mm/aaaa): ").strip()
    if not data:
        print("[red]Erro: A data não pode ser vazia")
        return
    
    if data not in treinos:
        treinos[data] = []
    
    while True:
        nome_ex = input("Nome do exercício: ").strip()
        if not nome_ex: break

        try:
            series = int(input("Número de séries: "))
            reps = int(input("Número de repetições: "))
            if series <= 0 or reps <= 0:
                print("[red]Erro: valores devem ser maiores que 0")
                continue
        except ValueError:
            print("[red]Digite apenas números inteiros")
            continue

        treinos[data].append({"nome": nome_ex, "series": series, "repeticoes": reps})
        
        # Salva no arquivo sempre que adicionar um exercício
        salvar_txt(treinos)
        
        print(Panel.fit(f"[green]'{nome_ex}' cadastrado!"))

        if input(f"Outro exercício em {data}? (S/N): ").upper() != "S":
            break

def listar_treinos():
    if not treinos:
        print("[yellow]Nenhum treino cadastrado!")
        return
    
    print(Panel.fit("[bold blue]Histórico de Datas"))
    for data in treinos:
        # Requisito: data e número de exercícios
        quantidade = len(treinos[data])
        print(f"📅 Data: [bold]{data}[/bold] | {quantidade} exercício(s)")

def exibir_treino():
    if not treinos:
        print("[yellow]Nenhum treino cadastrado!")
        return

    data_busca = input("Digite a data (dd/mm/aaaa) para detalhes: ").strip()
    
    if data_busca in treinos:
        print(Panel(f"Detalhes do dia {data_busca}", style="blue"))
        for ex in treinos[data_busca]:
            print(f" • [white]{ex['nome']}[/white] | {ex['series']}x{ex['repeticoes']}")
    else:
        print("[red]Data não encontrada.")

def listar_exercicios_mes():
    if not treinos:
        print("[yellow]Nenhum treino cadastrado!")
        return
    
    mes = input("Selecione o mês (01-12): ").strip()
    if len(mes) == 1: mes = "0" + mes
    
    encontrou = False
    for data in treinos:
        if data[3:5] == mes:
            encontrou = True
            print(f"\n[bold blue]Data: {data}[/bold blue]")
            for ex in treinos[data]:
                print(f" - {ex['nome']} ({ex['series']}x{ex['repeticoes']})")

    if not encontrou:
        print(f"[red]Nenhum treino encontrado para o mês {mes}.")

# --- INÍCIO ---
while True:
    aluno = input("Digite o nome do aluno: ").strip()
    if aluno.isalpha(): break
    print("[red]Nome inválido")

print(Panel(Align.center(f"Bem-vindo, {aluno.capitalize()}!"), title="[bold blue]Academia"))

menu_principal()