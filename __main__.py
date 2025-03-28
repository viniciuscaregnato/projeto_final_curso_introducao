""" Módulo __main__.py
Programa: Projeto Final
Descrição: Sua tarefa é organizar os arquivos "orcamento.xls", "orcamento.docx", "clientes.xls" e 
"clientes.doc" e "relatorio.doc" nas pastas planilhas e documentos de acordo com a extensão do arquivo.
Autor: Vinicius Caregnato Garcia
Versão: 0.0.1
Data: 22/03/2025
"""

# Importação de pacotes
import os

#importação de modulos
import organizacao
import endereco

def main():
    # Armazenamento de dados
    diretorio_atual: str=""
        
    # Entrada de dados
    diretorio_atual = endereco.endereco()  # Recebe o diretório atual
    arquivos_analisados = os.listdir(diretorio_atual)  # Lista de arquivos no diretório atual
    
    # Processamento e saída de dados
    organizacao.criar_pastas(arquivos_analisados)  # Cria as pastas necessárias
    organizacao.mover_arquivos(arquivos_analisados)  # Move os arquivos para as pastas corretas

if __name__ == "__main__":
    main()