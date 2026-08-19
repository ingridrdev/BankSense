from pathlib import Path

import pandas as pd
import streamlit as st


PASTA_PROJETO = Path(__file__).resolve().parent
CAMINHO_DADOS = (
    PASTA_PROJETO / "data" / "transacoes_analisadas.csv"
)


st.set_page_config(
    page_title="BankSense",
    page_icon="💳",
    layout="wide",
)


@st.cache_data
def carregar_dados():
    return pd.read_csv(CAMINHO_DADOS)


def formatar_reais(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("X", ".")

    return f"R$ {valor_formatado}"


transacoes = carregar_dados()

st.title("BankSense")
st.write("Painel de análise de risco de transações financeiras")

st.divider()

quantidade_transacoes = len(transacoes)
valor_total = transacoes["valor"].sum()
score_medio = transacoes["score_risco"].mean()

quantidade_alto_risco = (
    transacoes["classificacao"] == "ALTO RISCO"
).sum()

percentual_alto_risco = (
    quantidade_alto_risco / quantidade_transacoes
) * 100

coluna_1, coluna_2, coluna_3, coluna_4 = st.columns(4)

coluna_1.metric(
    label="Transações analisadas",
    value=quantidade_transacoes,
)

coluna_2.metric(
    label="Valor total",
    value=formatar_reais(valor_total),
)

coluna_3.metric(
    label="Score médio",
    value=f"{score_medio:.1f}",
)

coluna_4.metric(
    label="Transações de alto risco",
    value=quantidade_alto_risco,
    delta=f"{percentual_alto_risco:.1f}% da base",
    delta_color="inverse",
)

st.divider()

st.subheader("Distribuição por nível de risco")

ordem_classificacoes = [
    "BAIXO RISCO",
    "MÉDIO RISCO",
    "ALTO RISCO",
]

distribuicao = (
    transacoes["classificacao"]
    .value_counts()
    .reindex(ordem_classificacoes, fill_value=0)
)

st.bar_chart(
    distribuicao,
    color="#820AD1",
)

st.divider()

st.subheader("Transações analisadas")

opcoes_classificacao = st.multiselect(
    "Filtrar por classificação",
    options=ordem_classificacoes,
    default=ordem_classificacoes,
)

transacoes_filtradas = transacoes[
    transacoes["classificacao"].isin(opcoes_classificacao)
].copy()

transacoes_filtradas["valor"] = transacoes_filtradas[
    "valor"
].apply(formatar_reais)

st.dataframe(
    transacoes_filtradas,
    width="stretch",
    hide_index=True,
)

st.caption(
    f"{len(transacoes_filtradas)} transação(ões) encontrada(s)."
)

arquivo_download = transacoes.to_csv(
    index=False,
    encoding="utf-8-sig",
).encode("utf-8-sig")

st.download_button(
    label="Baixar resultados em CSV",
    data=arquivo_download,
    file_name="transacoes_analisadas.csv",
    mime="text/csv",
)

st.divider()

st.caption(
    "Projeto educacional com dados fictícios e regras simplificadas."
)