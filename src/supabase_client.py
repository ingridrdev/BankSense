import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from supabase import Client, create_client


PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_ENV = PASTA_PROJETO / ".env"

load_dotenv(ARQUIVO_ENV)


def criar_cliente_supabase() -> Client:
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_PUBLISHABLE_KEY")

    if not supabase_url or not supabase_key:
        raise RuntimeError(
            "As variáveis SUPABASE_URL e SUPABASE_PUBLISHABLE_KEY "
            "não foram encontradas."
        )

    return create_client(supabase_url, supabase_key)


def carregar_transacoes_supabase() -> pd.DataFrame:
    cliente = criar_cliente_supabase()

    resposta = (
        cliente.table("transacoes")
        .select("*")
        .order("id")
        .execute()
    )

    return pd.DataFrame(resposta.data)


if __name__ == "__main__":
    transacoes = carregar_transacoes_supabase()

    print(f"Transações encontradas: {len(transacoes)}")
    print(transacoes.head())