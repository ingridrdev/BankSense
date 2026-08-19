from pathlib import Path

import pandas as pd


PASTA_PROJETO = Path(__file__).resolve().parent.parent

CAMINHO_CSV = PASTA_PROJETO / "data" / "transacoes.csv"
CAMINHO_RESULTADO = PASTA_PROJETO / "data" / "transacoes_analisadas.csv"

transacoes = pd.read_csv(CAMINHO_CSV)


def calcular_risco(transacao):
    risco = 0

    if transacao["valor"] > 3000:
        risco += 40

    if transacao["hora"] < 6:
        risco += 30

    if transacao["tipo"].lower() == "pix":
        risco += 10

    if transacao["novo_dispositivo"].lower() == "sim":
        risco += 10

    if transacao["cidade_habitual"].lower() in ["não", "nao"]:
        risco += 10

    return risco


def classificar_risco(risco):
    if risco >= 60:
        return "ALTO RISCO"
    elif risco >= 30:
        return "MÉDIO RISCO"
    else:
        return "BAIXO RISCO"


# Calcula o score de cada transação
transacoes["score_risco"] = transacoes.apply(
    calcular_risco,
    axis=1
)

# Classifica cada transação
transacoes["classificacao"] = transacoes["score_risco"].apply(
    classificar_risco
)

# Salva o resultado em um novo arquivo CSV
transacoes.to_csv(
    CAMINHO_RESULTADO,
    index=False,
    encoding="utf-8-sig"
)

print("=== BankSense ===")
print("Análise automática das transações")
print("")

print(
    transacoes[
        [
            "valor",
            "hora",
            "tipo",
            "score_risco",
            "classificacao",
        ]
    ].to_string(index=False)
)

print("")
print("Quantidade de transações analisadas:", len(transacoes))
print("Resultado salvo em: data/transacoes_analisadas.csv")

# Cria indicadores gerais da análise
quantidade_baixo_risco = (
    transacoes["classificacao"] == "BAIXO RISCO"
).sum()

quantidade_medio_risco = (
    transacoes["classificacao"] == "MÉDIO RISCO"
).sum()

quantidade_alto_risco = (
    transacoes["classificacao"] == "ALTO RISCO"
).sum()

percentual_alto_risco = (
    quantidade_alto_risco / len(transacoes)
) * 100

valor_total = transacoes["valor"].sum()

valor_alto_risco = transacoes.loc[
    transacoes["classificacao"] == "ALTO RISCO",
    "valor"
].sum()

score_medio = transacoes["score_risco"].mean()


def formatar_reais(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("X", ".")

    return f"R$ {valor_formatado}"


print("")
print("======================================")
print("        RESUMO DA ANÁLISE")
print("======================================")
print("Baixo risco:", quantidade_baixo_risco)
print("Médio risco:", quantidade_medio_risco)
print("Alto risco:", quantidade_alto_risco)
print(f"Percentual de alto risco: {percentual_alto_risco:.1f}%")
print("Valor total analisado:", formatar_reais(valor_total))
print("Valor em alto risco:", formatar_reais(valor_alto_risco))
print(f"Score médio: {score_medio:.1f}")
print("======================================")