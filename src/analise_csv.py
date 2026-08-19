from pathlib import Path

import pandas as pd


PASTA_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_CSV = PASTA_PROJETO / "data" / "transacoes.csv"

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


transacoes["score_risco"] = transacoes.apply(calcular_risco, axis=1)

transacoes["classificacao"] = transacoes["score_risco"].apply(
    classificar_risco
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