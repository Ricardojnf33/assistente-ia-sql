import snowflake.connector
import pandas as pd
import os

def execute_sf_query(query):
    """
    Executa uma consulta SQL no Snowflake e retorna os resultados.

    Args:
        query (str): A consulta SQL a ser executada.

    Returns:
        DataFrame: Resultados da consulta.
    """
    conn = snowflake.connector.connect(
        user=os.getenv('SF_USER'),
        password=os.getenv('SF_PASSWORD'),
        account=os.getenv('SF_ACCOUNT'),
        warehouse=os.getenv('SF_WAREHOUSE'),
        database=os.getenv('SF_DATABASE'),
        schema=os.getenv('SF_SCHEMA'),
        role=os.getenv('SF_ROLE')
    )

    cur = conn.cursor()
    try:
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame(result, columns=[col[0] for col in cur.description])
        return df
    finally:
        cur.close()
        conn.close()
