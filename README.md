# BankSense

[![Abrir aplicativo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://banksense-ingridrdev.streamlit.app)

Sistema desenvolvido em Python para simular a análise de risco de transações financeiras.

O BankSense utiliza regras predefinidas para analisar características de uma transação, calcular um score de risco de 0 a 100 e classificá-la como baixo, médio ou alto risco.

## Aplicação publicada

Acesse o dashboard interativo:

**[Abrir o BankSense](https://banksense-ingridrdev.streamlit.app)**

## Objetivo

O projeto foi criado para praticar e demonstrar conhecimentos em:

* Python;
* análise de dados;
* manipulação de arquivos CSV;
* pandas;
* visualização de dados;
* criação de dashboards;
* lógica de programação;
* criação de regras de negócio;
* Git e GitHub;
* publicação de aplicações.

## Funcionalidades

* Análise manual de uma transação pelo terminal;
* Leitura automática de uma base de transações em CSV;
* Cálculo individual do score de risco;
* Classificação das transações;
* Geração de indicadores analíticos;
* Exibição dos resultados no terminal;
* Exportação dos resultados para um novo CSV;
* Gráfico com a distribuição dos níveis de risco;
* Dashboard interativo com Streamlit;
* Filtro por classificação de risco;
* Download dos resultados analisados.

## Indicadores do dashboard

O painel apresenta:

* Quantidade de transações analisadas;
* Valor total das transações;
* Score médio da base;
* Quantidade e percentual de transações de alto risco;
* Distribuição das transações por nível de risco;
* Tabela detalhada com filtros.

## Regras utilizadas

| Condição                          | Pontuação |
| --------------------------------- | --------: |
| Valor acima de R$ 3.000           |       +40 |
| Transação realizada antes das 6h  |       +30 |
| Transação realizada via PIX       |       +10 |
| Utilização de um novo dispositivo |       +10 |
| Transação fora da cidade habitual |       +10 |

## Classificação do risco

| Score       | Classificação |
| ----------- | ------------- |
| De 0 a 29   | Baixo risco   |
| De 30 a 59  | Médio risco   |
| De 60 a 100 | Alto risco    |

## Estrutura do projeto

```text
BankSense/
├── data/
│   ├── transacoes.csv
│   └── transacoes_analisadas.csv
├── reports/
│   └── distribuicao_risco.png
├── src/
│   ├── analise_csv.py
│   ├── main.py
│   └── visualizacao.py
├── app.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Tecnologias utilizadas

* Python 3;
* pandas;
* Matplotlib;
* Streamlit;
* Git;
* GitHub;
* Visual Studio Code;
* Streamlit Community Cloud.

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/ingridrdev/BankSense.git
```

### 2. Entre na pasta do projeto

```bash
cd BankSense
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Execute a análise manual

```bash
python src/main.py
```

### 5. Execute a análise automática do CSV

```bash
python src/analise_csv.py
```

### 6. Gere o gráfico de distribuição

```bash
python src/visualizacao.py
```

### 7. Execute o dashboard localmente

```bash
python -m streamlit run app.py
```

O painel será disponibilizado localmente em:

```text
http://localhost:8501
```

## Arquivos de dados

O arquivo `data/transacoes.csv` contém as transações fictícias utilizadas como entrada.

Após a execução da análise automática, o BankSense gera o arquivo `data/transacoes_analisadas.csv`, contendo os dados originais e as colunas:

* `score_risco`;
* `classificacao`.

## Exemplo de resultado

```text
 valor  hora          tipo  score_risco classificacao
3500.0     2           pix          100    ALTO RISCO
4500.0    11 transferencia           50   MÉDIO RISCO
 650.0    15           pix           10   BAIXO RISCO
```

## Visualização gerada

![Distribuição das transações por nível de risco](reports/distribuicao_risco.png)

## Próximas melhorias

* Validação e tratamento de dados inválidos;
* Criação de testes automatizados;
* Upload de bases pelo dashboard;
* Ampliação dos indicadores e filtros;
* Evolução das regras com base em padrões históricos;
* Experimentação com modelos de machine learning.

## Aviso

Este projeto possui finalidade exclusivamente educacional. Os dados são fictícios e as regras utilizadas são simplificadas. O BankSense não representa um sistema antifraude real e não deve ser utilizado para decisões financeiras.
