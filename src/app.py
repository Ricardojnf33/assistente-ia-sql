# pip install langchain streamlit openai snowflake-connector-python

#PIL
from langchain.llms import OpenAI
from langchain.chains import LLMChain

import os
from pathlib import Path
from PIL import Image
import streamlit as st
from langchain.prompts import load_prompt
from sql_execution import execute_sf_query

# Configurar a chave da API OpenAI
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def get_root_path():
    """
    Obtém o caminho raiz do projeto 'ai_sql_shop_assistent'.
    
    Retorna:
    - pathlib.Path: caminho raiz ou None se não for encontrado.
    """
    paths = [p for p in Path(__file__).parents if p.parts[-1] == "ai_sql_shop_assistent"]
    return paths[0] if paths else None

root_path = get_root_path()
if not root_path:
    st.error("Diretório 'ai_sql_shop_assistent' não encontrado!")
    raise SystemExit

# Interface de usuário
st.title("Assistente de SQL IA")
user_input = st.text_input("Escreva sua pergunta aqui")
tab_titles = ["Resultado", "Query", "Diagrama ERD"]
tabs = st.tabs(tab_titles)

# Carregar e exibir o diagrama ERD
erd_image_path = root_path / "images" / "ERD.png"
if erd_image_path.exists():
    erd_image = Image.open(erd_image_path)
    with tabs[2]:
        st.image(erd_image)
else:
    st.warning("Imagem ERD não encontrada!")

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
