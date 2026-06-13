# -*- coding: utf-8 -*-
"""
SISTEMA DE GERENCIAMENTO DE TREINOS DE ACADEMIA

Este é um projeto acadêmico desenvolvido em Python de Terminal para a primeira
cadeira de programação. Utiliza estruturas de dados fundamentais (dicionários, 
listas e conjuntos) para organizar exercícios de forma simples e intuitiva.

Estrutura de dados utilizada:
  treinos = {
      "data_em_texto": [
          {"nome": "Nome do Exercício", "series": 4, "repeticoes": 12}, ...
      ]
  }
"""

# Dicionário global para guardar todos os treinos.
# A chave é a Data (str) e o valor é uma Lista de Exercícios (list).
treinos = {}

def formatar_data(data_usuario):
    """
    Remove espaços adicionais e padroniza a data inserida pelo usuário.
    Espera-se receber no formato 'DD/MM/AAAA' ou similar.
    """
    return data_usuario.strip()

def adicionar_treino():
    """
    Cadastra uma dada data e permite ao usuário adicionar múltiplos exercícios
    a ela de maneira interativa. Cada exercício possui nome, séries e repetições.
    """
    print("\n========================================")
    print("           ADICIONAR TREINO             ")
    print("========================================")
    
    data = input("Digite a data do treino (DD/MM/AAAA): ")
    data = formatar_data(data)
    
    if not data:
        print("Erro: A data não pode ser vazia.")
        return
        
    # Se já não houver treino nessa data, inicializamos uma lista vazia
    if data not in treinos:
        treinos[data] = []
        
    while True:
        print("\n--- Novo Exercício ---")
        nome = input("Nome/Descrição do exercício: ").strip()
        if not nome:
            print("Erro: O nome do exercício não pode ser vazio.")
            continue
            
        try:
            series = int(input("Número de séries (ex: 3, 4): "))
            repeticoes = int(input("Número de repetições (ex: 10, 12): "))
            
            if series <= 0 or repeticoes <= 0:
                print("Erro: Séries e repetições devem ser números inteiros maiores que zero.")
                continue
        except ValueError:
            print("Erro: Digite apenas números inteiros válidos para séries e repetições.")
            continue
            
        # Criamos a estrutura de dicionário para representar o exercício individual
        exercicio = {
            "nome": nome,
            "series": series,
            "repeticoes": repeticoes
        }
        
        # Adiciona na lista associada à respectiva data
        treinos[data].append(exercicio)
        print(f"\nSucesso: Exercício '{nome}' cadastrado para o dia {data}!")
        
        # Pergunta ao usuário se quer continuar adicionando na mesma data
        loop_opcao = input("\nDeseja adicionar outro exercício nesta mesma data ({})? (S/N): ").format(data).strip().upper()
        if loop_opcao != "S":
            break

def listar_treinos():
    """
    Mostra um resumo de todos os treinos cadastrados no sistema.
    Informa a data e o respectivo número de exercícios existentes nela.
    """
    print("\n========================================")
    print("          RESUMO DOS TREINOS            ")
    print("========================================")
    
    if not treinos:
        print("Ainda não há nenhum treino registrado no sistema.")
        return
        
    print(f"{'Data':<15} | {'Nº de Exercícios':<20}")
    print("-" * 40)
    
    # Percorre o dicionário, exibindo a chave (data) e o tamanho da lista (quantidade de exercícios)
    for data, lista_exercicios in sorted(treinos.items()):
        total_exercicios = len(lista_exercicios)
        print(f"{data:<15} | {total_exercicios:<20} exercícios")
    print("-" * 40)

def exibir_treino():
    """
    Solicita ao usuário uma data e lista detalhadamente todos os exercícios 
    daquele dia com suas respectivas séries e repetições.
    """
    print("\n========================================")
    print("           DETALHES DO TREINO           ")
    print("========================================")
    
    if not treinos:
        print("Ainda não há treinos registrados no sistema.")
        return
        
    data = input("Digite a data do treino que deseja visualizar (DD/MM/AAAA): ")
    data = formatar_data(data)
    
    if data in treinos:
        print(f"\nTreino do dia: {data}")
        print("-" * 60)
        print(f"{'Exercício':<30} | {'Séries':<10} | {'Repetições':<12}")
        print("-" * 60)
        
        for exercicio in treinos[data]:
            print(f"{exercicio['nome']:<30} | {exercicio['series']:<10} | {exercicio['repeticoes']:<12}")
        print("-" * 60)
    else:
        print(f"Não habilitado: Nenhum treino foi localizado para a data '{data}'.")

def listar_exercicios_no_mes():
    """
    Lista todos os nomes de exercícios realizados em um mês específico,
    removendo duplicatas. Utiliza a estrutura 'Set' (conjunto) do Python.
    """
    print("\n========================================")
    print("      EXERCÍCIOS REALIZADOS NO MÊS      ")
    print("========================================")
    
    if not treinos:
        print("Ainda não há treinos registrados no sistema.")
        return
        
    pesquisa = input("Digite o mês (MM) ou o mês/ano (MM/AAAA) para buscar: ").strip()
    
    if not pesquisa:
        print("Erro: A busca não pode ser vazia.")
        return
        
    # Usamos a estrutura de Set (conjunto) que por definição não aceita duplicados.
    # Isso resolve com maestria a exigência de ser "sem repetição".
    exercicios_unicos = set()
    
    # Varre todo o dicionário de treinos
    for data, lista_exercicios in treinos.items():
        # Verifica se o termo digitado está presente na data cadastrada (Ex: '06' em '12/06/2026')
        if pesquisa in data:
            for exercicio in lista_exercicios:
                # Adicionamos apenas o nome do exercício ao conjunto
                exercicios_unicos.add(exercicio["nome"])
                
    if exercicios_unicos:
        print(f"\nExercicios únicos encontrados no período '{pesquisa}':")
        print("-" * 50)
        # Exibe os exercícios em ordem alfabética ordenada
        for indice, nome_exercicio in enumerate(sorted(exercicios_unicos), 1):
            print(f"{indice}. {nome_exercicio}")
        print("-" * 50)
    else:
        print(f"Nenhum treino/exercício encontrado para o período '{pesquisa}'.")

def menu_principal():
    """
    Loop principal do menu interativo no terminal.
    """
    while True:
        print("\n========================================")
        print("     SISTEMA DE TREINOS DE ACADEMIA     ")
        print("========================================")
        print("1. Adicionar Treino")
        print("2. Listar Treinos (Resumo)")
        print("3. Exibir Treino Completo (de um dia)")
        print("4. Listar Exercícios no Mês (sem repetições)")
        print("5. Sair do Programa")
        print("========================================")
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            adicionar_treino()
        elif opcao == "2":
            listar_treinos()
        elif opcao == "3":
            exibir_treino()
        elif opcao == "4":
            listar_exercicios_no_mes()
        elif opcao == "5":
            print("\nFinalizando o sistema de academia... Bons treinos!")
            break
        else:
            print("Opção inválida! Escolha um número representável entre 1 e 5.")

# Garante que o programa executa o menu apenas se rodar diretamente
if __name__ == "__main__":
    menu_principal()
