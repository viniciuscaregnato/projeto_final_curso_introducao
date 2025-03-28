""" Módulo criar_pastas.py
Programa: Projeto Final
Descrição: Este módulo cria subpastas no diretorio atual, e organiza os arquivos dentro de cada uma, conforme sua extensao.
Autor: Vinicius Caregnato Garcia
Versão: 0.0.1
Data: 22/03/2025
"""

import os
import shutil

def criar_pastas(arquivos_analisados) -> list:
    """Cria as pastas 'planilhas' e 'documentos' somente se houver arquivos correspondentes."""
    if any(i.endswith('.xls') for i in arquivos_analisados): # Verifica se há arquivos .xls
        os.makedirs("planilhas", exist_ok=True)  # Cria a pasta 'planilhas' caso haja arquivos .xls
    
    if any(i.endswith('.doc') or i.endswith('.docx') for i in arquivos_analisados): # Verifica se há arquivos .doc ou .docx
        os.makedirs("documentos", exist_ok=True)  # Cria a pasta 'documentos' caso haja arquivos .doc ou .docx

def mover_arquivos(arquivos_analisados) -> list:
    """Move os arquivos para as devidas pastas conforme suas extensões."""
    for i in arquivos_analisados:
        if i.endswith('.xls'):
            destino = "planilhas"  # se houver arquivo com extensao .xls relaciona "destino" com "planilhas"
        elif i.endswith('.doc') or i.endswith('.docx'):
            destino = "documentos"  # se houver arquivo com extensao .doc ou .docx, relaciona "destino" com "documentos"
        else:
            continue  # Ignora arquivos que não são .xls, .doc ou .docx

        # Move o arquivo para a pasta apropriada
        shutil.move(i, os.path.join(destino, i))
        print(f"O arquivo '{i}' foi movido para a pasta '{destino}'")
