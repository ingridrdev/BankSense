from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PASTA_PROJETO = Path(__file__).resolve().parent.parent

CAMINHO_DADOS = (
    PASTA_PROJETO / "data" / "transacoes_analisadas.csv"
)

PASTA_RELATORIOS = PASTA_PROJETO / "reports"
CAMINHO_GRAFICO = PASTA_RELATORIOS / "distribuicao_risco.png"

# Cria a pasta reports caso ela ainda não exista
PASTA_RELATORIOS.mkdir(exist_ok=True)

# Lê os resultados gerados pela análise
transacoes = pd.read_csv(CAMINHO_DADOS)

ordem_classificacoes = [
    "BAIXO RISCO",
    "MÉDIO RISCO",
    "ALTO RISCO",
]

quantidades = (
    transacoes["classificacao"]
    .value_counts()
    .reindex(ordem_classificacoes, fill_value=0)
)

cores = [
    "#2E8B57",
    "#F4A261",
    "#D62828",
]

plt.figure(figsize=(9, 5))

barras = plt.bar(
    quantidades.index,
    quantidades.values,
    color=cores,
    width=0.6,
)

plt.title(
    "Distribuição das transações por nível de risco",
    fontsize=14,
    fontweight="bold",
)

plt.xlabel("Classificação")
plt.ylabel("Quantidade de transações")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3,
)

for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 0.1,
        str(int(altura)),
        ha="center",
        fontweight="bold",
    )

plt.tight_layout()

plt.savefig(
    CAMINHO_GRAFICO,
    dpi=300,
    bbox_inches="tight",
)

plt.show()

print("Gráfico gerado com sucesso!")
print("Arquivo salvo em: reports/distribuicao_risco.png")