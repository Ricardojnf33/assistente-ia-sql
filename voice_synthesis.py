# voice_synthesis.py

import os
import requests
from pydub import AudioSegment
from io import BytesIO

# Supondo que estamos usando uma API genérica de síntese de voz
API_URL = "https://api.sintese-voz.com/v1/voz"
API_KEY = os.getenv("API_KEY_SYNTHESIS")

def sintetizar_voz(texto):
    """
    Converte texto em áudio usando a API de síntese de voz escolhida.

    Args:
        texto (str): Texto a ser convertido em áudio.

    Returns:
        AudioSegment: Objeto de áudio que pode ser reproduzido ou salvo.
    """
    if not API_KEY:
        raise ValueError("API key para síntese de voz não configurada.")

    # Configura os dados de requisição para a API
    dados = {
        "texto": texto,
        "formato": "mp3",
        "velocidade": "normal",
        "linguagem": "pt-br"
    }

    headers = {"Authorization": f"Bearer {API_KEY}"}

    # Faz a requisição à API de síntese de voz
    resposta = requests.post(API_URL, json=dados, headers=headers)

    if resposta.status_code == 200:
        # Converte a resposta em áudio
        audio_stream = BytesIO(resposta.content)
        audio = AudioSegment.from_file(audio_stream, format="mp3")
        return audio
    else:
        # Trata erros de requisição
        raise Exception(f"Erro na síntese de voz: {resposta.status_code}")

def salvar_audio(audio, caminho_arquivo):
    """
    Salva o áudio em um arquivo.

    Args:
        audio (AudioSegment): Objeto de áudio a ser salvo.
        caminho_arquivo (str): Caminho para salvar o arquivo de áudio.
    """
    audio.export(caminho_arquivo, format="mp3")

# Exemplo de uso
if __name__ == "__main__":
    texto_para_sintetizar = "Olá, bem-vindo ao assistente de SQL IA."
    audio = sintetizar_voz(texto_para_sintetizar)
    salvar_audio(audio, "saida_audio.mp3")
