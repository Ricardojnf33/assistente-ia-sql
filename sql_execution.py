import os
import snowflake.connector
import pandas as pd
import logging

from dotenv import load_dotenv
load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Configure o logging para o nível DEBUG
logging.basicConfig(level=logging.DEBUG)

# Carregar as credenciais do Snowflake de variáveis de ambiente
SF_USER = os.getenv('SF_USER')
SF_PASSWORD = os.getenv('SF_PASSWORD')
SF_ACCOUNT = os.getenv('SF_ACCOUNT')
SF_WAREHOUSE = os.getenv('SF_WAREHOUSE')
SF_DATABASE = os.getenv('SF_DATABASE')
SF_SCHEMA = os.getenv('SF_SCHEMA')
SF_ROLE = os.getenv('SF_ROLE')

# Verificar se todas as variáveis de ambiente necessárias estão configuradas
if not all([SF_USER, SF_PASSWORD, SF_ACCOUNT, SF_WAREHOUSE, SF_DATABASE, SF_SCHEMA, SF_ROLE]):
    raise ValueError("As credenciais do Snowflake não foram configuradas corretamente.")

def execute_sf_query(p_sql):
    # Parâmetros de conexão Snowflake a partir das variáveis de ambiente
    connection_params = {
        'user': SF_USER,
        'password': SF_PASSWORD,
        'account': SF_ACCOUNT,
        'warehouse': SF_WAREHOUSE,
        'database': SF_DATABASE,
        'schema': SF_SCHEMA,
        'role': SF_ROLE
    }

    query = p_sql

    # Inicializando as variáveis
    cur = None
    conn = None

    try:
        # Estabelecer uma conexão com Snowflake
        conn = snowflake.connector.connect(**connection_params)

        # Criar um objeto cursor
        cur = conn.cursor()

        # Executar a consulta
        cur.execute(query)

        # Buscar todos os resultados
        query_results = cur.fetchall()

        # Obter nomes de colunas da descrição do cursor
        column_names = [col[0] for col in cur.description]

        # Criar um DataFrame Pandas
        data_frame = pd.DataFrame(query_results, columns=column_names)

        return data_frame

    except snowflake.connector.errors.ProgrammingError as pe:
        print("Query Compilation Error:", pe)
        return("Query compilation error")

    except snowflake.connector.errors.DatabaseError as de:
        print("Erro no Banco de Dados Snowflake:", de)
        return {"error": "Erro no Banco de Dados Snowflake", "details": str(de)}

    except Exception as e:
        print("Ocorreu um erro:", e)
        return {"error": "Ocorreu um erro", "details": str(e)}

    finally:
        # Fechar o cursor e conexão
        if cur:
            cur.close()
        if conn:
            conn.close()

