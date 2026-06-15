from rich.prompt import IntPrompt
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print
from SavedData import salvar_txt
from datetime import datetime, timedelta

def adicionar_treino(treinos, aluno):
    # ===== VALIDAÇÃO DA DATA =====
    dataAtual = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    recebeData = Prompt.ask("[white]Data (dd/mm/aaaa)[/white]").strip()
    if len(recebeData.split()) < 3:
        print("[red]Erro: Insiria uma data completa.")
        return

    dia,mes,ano = recebeData.split()
    dia = dia.zfill(2)
    mes = mes.zfill(2)
    data = dia+" "+mes+" "+ano

    #===== VERIFICA SE A DATA NAO ESTA VAZIA =====
    if not data:
        print(Panel.fit("[red]Erro: A data nao pode ser vazia"))
        return
    
    #===== VERIFICA SE NA DATA CONTEM APENAS NUMEROS =====
    elif not data.split()[0].isnumeric() or not data.split()[1].isnumeric() or not data.split()[2].isnumeric():
        print(Panel.fit("[red]Erro: Insira apenas números válidos."))
        return
    
    #===== VERIFICA SE A DATA CONDIZ COM O DIA ATUAL =====
    dataVerify =  datetime.strptime(data.replace(" ","/"), "%d/%m/%Y")
    if dataVerify < dataAtual:
        print(Panel.fit("[red]Erro: Data inválida, quer uma maquina do tempo?"))
        return
    
    #===== VERIFICA SE E UMA DATA VALIDA =====
    elif len(data) != 10:
        print(Panel.fit("[red]Erro: Formato de data invalido, tente novamente!"))
        return 
    elif int(data.split()[0]) not in list(range(1,32)) or int(data.split()[1]) not in list(range(1,13)):
        print(Panel.fit("[red]Erro: Data inválida."))
        return

    # ===== CRIA DATA NO DICIONARIO (Memória local) =====
    if data not in treinos:
        treinos[data] = []

    # ===== CADASTRA OS EXERCÍCIOS =====
    while True:
        nome_ex = Prompt.ask("[white]Nome do exercício").strip()
        if not nome_ex: break

        try:
            series = IntPrompt.ask("[white]Número de séries")
            reps = IntPrompt.ask("[white]Número de repetições")
            if series <= 0 or reps <= 0:
                print(Panel.fit("[red]Erro: valores devem ser maiores que 0"))
                continue
        except ValueError:
            print(Panel.fit("[red]Digite apenas números inteiros"))
            continue

        # 1. Cria o dicionário do exercício
        novo_exercicio = {"nome": nome_ex, "series": series, "repeticoes": reps}
        
        # 2. Adiciona na memória (para uso imediato no programa)
        treinos[data].append(novo_exercicio)
        
        # 3. SALVA NO ARQUIVO TXT (Passando o aluno logado, a data e o exercício)
        salvar_txt(aluno, data, novo_exercicio)
        
        print(Panel.fit(f"[green]'{nome_ex}' cadastrado e salvo com sucesso!"))

        if Prompt.ask(f"[yellow]Deseja adicionar outro exercício em {data.replace(" ","/")}? (S/N)").upper() != "S":
            break