import snowflake.connector
import pandas as pd

def execute_sf_query(p_sql):
    # Parâmetros de conexão Snowflake
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
    conn = None
    cur = None

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
