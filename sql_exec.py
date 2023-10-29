import os
from astra_db.rest import AstraDB
from dotenv import load_dotenv  

load_dotenv()

# Credenciais AstraDB
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")
ASTRA_DB_REGION = os.getenv("ASTRA_DB_REGION") 
ASTRA_DB_KEYSPACE = "shopping_db"
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")

def connect_astra():

  try:
    # Cria cliente AstraDB 
    astra_client = AstraDB(ASTRA_DB_ID, ASTRA_DB_REGION, ASTRA_DB_APPLICATION_TOKEN)

    # Faz conexão com o banco
    db = astra_client.connect(ASTRA_DB_KEYSPACE)
    
    return db

  except Exception as e:
    print(f"Erro ao conectar ao Astra DB: {e}")
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
  Executa uma query no Astra DB
  """

  try:
    cur = conn.cursor()
    cur.execute(query)  
    rows = cur.fetchall()
    return rows

  except Exception as e:
    print(f"Erro ao executar query: {e}")
    return None 


def get_df_from_sql(conn, query):
  """
  Retorna um DataFrame da query
  """

  try:
    return pd.read_sql(query, conn)
  
  except Exception as e: 
    print(f"Erro ao executar query: {e}")
    return None
