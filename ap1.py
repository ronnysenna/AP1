# Nome: RONIELLE DE SENA SILVA
# Matrícula: 2024013010

# Importação de bibliotecas nativas
import os                 # Para manipular caminhos e verificar existência de arquivos
import re                 # Para expressões regulares (extração de números)
import statistics         # Para cálculos estatísticos (média, mediana, etc.)

# Importação de bibliotecas de terceiros
from docx import Document         # Para leitura de arquivos .docx (Word)
from PyPDF2 import PdfReader      # Para leitura de arquivos .pdf

# Caminho da pasta onde o programa vai procurar os arquivos de dados
CAMINHO = "/Users/ronnysenna/Desktop/AP1/Documento"

# Função para encontrar um arquivo válido com nome "dados" e extensão .pdf, .docx ou .txt
def encontrar_arquivo():
    for ext in ['pdf', 'docx', 'txt']:  # Testa cada uma das extensões permitidas
        caminho_arquivo = os.path.join(CAMINHO, f'dados.{ext}')
        if os.path.isfile(caminho_arquivo):  # Verifica se o arquivo existe
            return caminho_arquivo
    return None  # Retorna None se nenhum arquivo válido for encontrado

# Função para ler um arquivo PDF e retornar suas linhas de texto
def ler_arquivo_pdf(caminho):
    try:
        reader = PdfReader(caminho)
        texto = ""
        for page in reader.pages:
            texto += page.extract_text() + "\n"  # Junta o texto de todas as páginas
        return texto.splitlines()  # Divide o texto em linhas
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return []

# Função para ler um arquivo DOCX (Word) e retornar suas linhas
def ler_arquivo_docx(caminho):
    try:
        doc = Document(caminho)
        return [p.text for p in doc.paragraphs if p.text.strip()]  # Retorna apenas parágrafos com texto
    except Exception as e:
        print(f"Erro ao ler o DOCX: {e}")
        return []

# Função para ler um arquivo TXT e retornar suas linhas
def ler_arquivo_txt(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except Exception as e:
        print(f"Erro ao ler o TXT: {e}")
        return []

# Função para extrair todos os números inteiros de uma lista de linhas de texto
def extrair_numeros(linhas):
    numeros = []
    for linha in linhas:
        encontrados = re.findall(r'\d+', linha)  # Encontra todos os números inteiros na linha
        numeros.extend(map(int, encontrados))    # Converte para inteiro e adiciona na lista
    return numeros

# Função para calcular e exibir estatísticas com base na lista de números
def calcular_estatisticas(numeros):
    print("\n=== Estatísticas ===")
    print(f"Média: {statistics.mean(numeros):.2f}")     # Calcula a média
    print(f"Mediana: {statistics.median(numeros)}")     # Calcula a mediana
    print(f"Somatório: {sum(numeros)}")                 # Soma todos os números
    print(f"Maior valor: {max(numeros)}")               # Mostra o maior número
    print(f"Menor valor: {min(numeros)}")               # Mostra o menor número

# Função principal que organiza o fluxo do programa
def main():
    print("Verificando arquivo...")
    caminho = encontrar_arquivo()

    if not caminho:
        print("Arquivo 'dados.pdf', 'dados.docx' ou 'dados.txt' não encontrado na pasta 'Documento'.")
        return

    print(f"Arquivo encontrado: {caminho}")

    # Chama a função de leitura conforme a extensão do arquivo
    if caminho.endswith('.pdf'):
        linhas = ler_arquivo_pdf(caminho)
    elif caminho.endswith('.docx'):
        linhas = ler_arquivo_docx(caminho)
    elif caminho.endswith('.txt'):
        linhas = ler_arquivo_txt(caminho)
    else:
        print("Formato de arquivo não suportado.")
        return

    # Verifica se foi possível ler alguma linha
    if not linhas:
        print("O arquivo está vazio ou não foi possível ler seu conteúdo.")
        return

    # Extrai os números das linhas lidas
    numeros = extrair_numeros(linhas)

    # Verifica se encontrou algum número
    if not numeros:
        print("Nenhum número válido encontrado no arquivo.")
        return

    # Calcula e exibe as estatísticas
    calcular_estatisticas(numeros)

# Executa a função principal quando o script for rodado diretamente
if __name__ == "__main__":
    main()
