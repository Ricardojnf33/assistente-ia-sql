import os
import psycopg2
import psycopg2.extras
import pandas as pd
from dotenv import load_dotenv

load_dotenv() 

# Carrega credenciais do PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")  
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


def connect_to_postgres():
  """
  Conecta ao banco de dados PostgreSQL
  """

  try:
    conn = psycopg2.connect(
      host=DB_HOST,
      database=DB_NAME,
      user=DB_USER,
      password=DB_PASS  
    )
    return conn

  except Exception as e:
    print(f"Erro ao conectar no PostgreSQL: {e}")
    return None


def close_connection(conn):
  """
  Fecha a conexão com o PostgreSQL
  """

  try:
    conn.close()
    print("Conexão fechada com sucesso!")
  except Exception as e:
    print(f"Erro ao fechar conexão: {e}")


def execute_query(conn, query):
  """
  Executa uma query SQL no banco
  """

  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(query)

  rows = cur.fetchall()
  conn.commit()

  return rows


def get_df_from_sql(conn, query):
  """
  Executa uma query SQL e retorna um DataFrame
  """

  try:
    return pd.read_sql(query, conn)
  
  except Exception as e:
    print(f"Erro ao executar query: {e}")
    return None
