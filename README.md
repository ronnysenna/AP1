# 📊 AP1 - Estatísticas de Arquivos (.pdf, .docx ou .txt)

### 👤 Autor: Ronielle de Sena Silva  

---

## 📌 Descrição

Este projeto em Python lê arquivos contendo números (um por linha ou misturados ao texto), nos formatos `.pdf`, `.docx` ou `.txt`, e realiza o cálculo de estatísticas simples:

- Média
- Mediana
- Somatório
- Maior valor
- Menor valor

O programa é capaz de identificar automaticamente o tipo de arquivo e realizar a leitura adequada, extraindo corretamente os números.

---

## 📁 Estrutura do Projeto

```
AP1/
├── ap1.py                  # Script principal
├── Documento/              # Pasta onde o arquivo de dados deve ser colocado
│   └── dados.docx          # Pode ser dados.pdf, dados.txt ou dados.docx
└── README.md               # Este arquivo
```

---

## ⚙️ Requisitos

Antes de executar, você precisa instalar as bibliotecas necessárias:

### Instalação via pip:

```bash
pip install python-docx PyPDF2
```

Ou com um arquivo de dependências (se tiver criado):

```bash
pip install -r requirements.txt
```

---

## 🚀 Como Executar

1. Crie uma pasta chamada `Documento` (se ainda não existir) no mesmo nível do `ap1.py`.
2. Coloque dentro dela **um arquivo chamado** `dados.docx`, `dados.pdf` ou `dados.txt`.
3. No terminal, navegue até a pasta do projeto e execute:

```bash
python ap1.py
```

---

## ✅ Exemplo de Saída

```
Verificando arquivo...
Arquivo encontrado: SEU CAMINHO/Documento/dados.docx

=== Estatísticas ===
Média: 34.00
Mediana: 20
Somatório: 170
Maior valor: 100
Menor valor: 5
```

---

## 📦 Bibliotecas Utilizadas

- `os` — manipulação de arquivos e caminhos
- `re` — expressões regulares para extrair números
- `statistics` — cálculo estatístico
- `python-docx` — leitura de arquivos .docx
- `PyPDF2` — leitura de arquivos .pdf

---

## ℹ️ Observações

- O arquivo deve obrigatoriamente se chamar `dados.pdf`, `dados.docx` ou `dados.txt`
- O script trata erros como:
  - Arquivo não encontrado
  - Arquivo vazio
  - Conteúdo inválido
- Os números extraídos devem ser inteiros (ex: 10, 20, 35...)

---

## 🎓 Projeto desenvolvido para a AP1 de programação
