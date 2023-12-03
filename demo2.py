import streamlit as st
from sql_execution import execute_sf_query
from voice_synthesis import sintetizar_voz_google, salvar_audio

# Configuração inicial do Streamlit
st.title("Assistente de SQL IA")

# Entrada do usuário
user_input = st.text_input("Digite sua consulta SQL aqui:")

# Execução da consulta SQL
if st.button("Executar"):
    if user_input:
        try:
            result_df = execute_sf_query(user_input)
            st.write(result_df)
        except Exception as e:
            st.error(f"Erro ao executar a consulta: {e}")

        # Opção para síntese de voz
        if st.button("Ouvir Resposta"):
            try:
                audio_bytes = sintetizar_voz_google(str(result_df))
                audio_file = "output.mp3"
                salvar_audio(audio_bytes, audio_file)
                st.audio(audio_file)
            except Exception as e:
                st.error(f"Erro na síntese de voz: {e}")
    else:
        st.warning("Por favor, insira uma consulta SQL.")
