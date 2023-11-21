# pip install langchain streamlit openai snowflake-connector-python

# PIL
import os
from pathlib import Path
from PIL import Image
# Removida a importação de app_secrets
from langchain.prompts import load_prompt
from sql_execution import execute_sf_query
import streamlit as st

from langchain.llms import OpenAI
from langchain.chains import LLMChain

#from dotenv import load_dotenv
#load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env


# Configurar a chave da API OpenAI a partir de variáveis de ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("A chave da API OpenAI não foi configurada.")

# Define o caminho raiz baseado na localização do arquivo
root_path = [p for p in Path(__file__).parents if p.parts[-1] == "assistente-ia-sql"][0]

# Interface de usuário
st.title("Assistente de SQL IA")
user_input = st.text_input("Escreva sua pergunta aqui")
tab_titles = ["Resultado", "Query", "Diagrama ERD"]
tabs = st.tabs(tab_titles)

# Carregar e exibir o diagrama ERD
erd_image = Image.open(f'{root_path}/images/ERD.png')
with tabs[2]:
    st.image(erd_image)

# Configurar e usar a cadeia de geração de SQL
prompt_path = root_path / "prompts" / "prompt_template.yaml"
if prompt_path.exists():
    prompt_template = load_prompt(prompt_path)
    llm = OpenAI(temperature=0)
    sql_generation_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

    if user_input:
        sql_query = sql_generation_chain(user_input)
        result = execute_sf_query(sql_query['text'])
        with tabs[0]:
            st.write(result)
        with tabs[1]:
            st.write(sql_query['text'])
else:
    st.error("Arquivo de prompt não encontrado!")
