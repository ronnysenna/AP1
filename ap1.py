# Nome: RONIELLE DE SENA SILVA
# Matrícula: 2024013010

import os
import re
import statistics

from docx import Document         
from PyPDF2 import PdfReader      


CAMINHO = "/Users/ronnysenna/Desktop/AP1/Documento"

def encontrar_arquivo():
    for ext in ['pdf', 'docx', 'txt']:
        caminho_arquivo = os.path.join(CAMINHO, f'dados.{ext}')
        if os.path.isfile(caminho_arquivo):
            return caminho_arquivo
    return None

def ler_arquivo_pdf(caminho):
    try:
        reader = PdfReader(caminho)
        texto = ""
        for page in reader.pages:
            texto += page.extract_text() + "\n"
        return texto.splitlines()
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return []

def ler_arquivo_docx(caminho):
    try:
        doc = Document(caminho)
        return [p.text for p in doc.paragraphs if p.text.strip()]
    except Exception as e:
        print(f"Erro ao ler o DOCX: {e}")
        return []

def ler_arquivo_txt(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except Exception as e:
        print(f"Erro ao ler o TXT: {e}")
        return []

def extrair_numeros(linhas):
    numeros = []
    for linha in linhas:
        encontrados = re.findall(r'\d+', linha)
        numeros.extend(map(int, encontrados))
    return numeros

def calcular_estatisticas(numeros):

    print("\n=== Estatísticas ===")
    print(f"Média: {statistics.mean(numeros):.2f}")
    print(f"Mediana: {statistics.median(numeros)}")
    print(f"Somatório: {sum(numeros)}")
    print(f"Maior valor: {max(numeros)}")
    print(f"Menor valor: {min(numeros)}")

def main():
    print("Verificando arquivo...")
    caminho = encontrar_arquivo()

    if not caminho:
        print("Arquivo 'dados.pdf', 'dados.docx' ou 'dados.txt' não encontrado na pasta 'Documento'.")
        return

    print(f"Arquivo encontrado: {caminho}")

    if caminho.endswith('.pdf'):
        linhas = ler_arquivo_pdf(caminho)
    elif caminho.endswith('.docx'):
        linhas = ler_arquivo_docx(caminho)
    elif caminho.endswith('.txt'):
        linhas = ler_arquivo_txt(caminho)
    else:
        print("Formato de arquivo não suportado.")
        return

    if not linhas:
        print("O arquivo está vazio ou não foi possível ler seu conteúdo.")
        return

    numeros = extrair_numeros(linhas)

    if not numeros:
        print("Nenhum número válido encontrado no arquivo.")
        return

    calcular_estatisticas(numeros)

if __name__ == "__main__":
    main()
