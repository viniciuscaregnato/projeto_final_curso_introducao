""" Módulo endereco.py
Programa: Projeto Final
Descrição: Este módulo solicita o diretorio desejado, para torná-lo o diretório atual. Então, lista os arquivos que estão nele, para posterior organização.
Versão: 0.0.1
Data: 22/03/2025
"""

import os

def endereco() -> str:
    diretorio_analisado = input("Digite o endereço da pasta que deseja organizar: ") # o usuario cola o endereço da pasta a ser organizada
    os.chdir(f"{diretorio_analisado}") # aqui o endereço da pasta informada pelo usuario se torna a pasta "atual" trabalhada

