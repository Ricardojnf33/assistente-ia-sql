import streamlit as st
from sql_exec import execute_query
from prompts.prompt import load_prompt
import openai

# Layout do app
st.title("Assistente de SQL por Voz")
st.write("Faça uma pergunta em linguagem natural sobre o banco de dados:")

# Entrada de pergunta do usuário
question = st.text_input("Sua pergunta:")

if question:

  # Carrega prompt GPT
  prompt = load_prompt()  

  # Gera query SQL com GPT
  openai.api_key = os.getenv("OPENAI_API_KEY")
  gpt = openai.Completion.create(engine="text-davinci-002", prompt=prompt + question)
  sql_query = gpt.choices[0].text
  
  # Executa query no banco
  result = execute_query(sql_query)

  # Exibe resultado
  st.write("Resultado:", result)

  st.code(sql_query)
