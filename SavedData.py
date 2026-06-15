import os

arquivo = "treinos.txt"

def salvar_txt(nome_aluno, data_treino, ex):
    #Salva um único exercício por vez no arquivo.
    with open(arquivo, "a", encoding="utf-8") as f:
        # Removi o espaço extra antes de "Aluno" para não dar erro no startswith
        linha = f"Aluno: {nome_aluno} |Data {data_treino}| Nome: {ex['nome']}| |Series: {ex['series']}| |Repeticoes: {ex['repeticoes']}|\n"
        f.write(linha)

def carregar_txt(aluno_atual):
    #Lê o arquivo TXT e reconstrói o dicionário filtrando pelo nome do aluno.
    dados_carregados = {}
    if not os.path.exists(arquivo):
        return {}

    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            if "|" in linha:
                partes = linha.split("|")
                
                # Pegamos a primeira parte: "Aluno: gui " ou "Aluno: guilherme "
                # Removemos o "Aluno: " e os espaços extras para comparar
                nome_no_arquivo = partes[0].replace("Aluno:", "").strip()

                # AGORA A COMPARAÇÃO É EXATA: "gui" == "gui" (True) | "gui" == "guilherme" (False)
                if nome_no_arquivo.lower() == aluno_atual.lower():
                    try:
                        data = partes[1].replace("Data ", "").strip()
                        nome = partes[2].replace(" Nome: ", "").strip()
                        series = int(partes[4].replace("Series: ", "").strip())
                        reps = int(partes[6].replace("Repeticoes: ", "").strip())

                        if data not in dados_carregados:
                            dados_carregados[data] = []
                        
                        dados_carregados[data].append({
                            "nome": nome,
                            "series": series,
                            "repeticoes": reps
                        })
                    except Exception:
                        continue
    return dados_carregados