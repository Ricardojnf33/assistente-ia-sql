# pip install --upgrade google-cloud-texttospeech

# voice_synthesis.py

from google.cloud import texttospeech
import os

# Configuração da chave da API (supondo que a chave da API esteja definida como uma variável de ambiente)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "caminho_para_sua_chave_de_api.json"

def sintetizar_voz_google(texto, idioma="pt-BR", genero_voz=texttospeech.SsmlVoiceGender.NEUTRAL):
    """
    Converte texto em áudio usando a API do Google Text-to-Speech.

    Args:
        texto (str): Texto a ser convertido em áudio.
        idioma (str): Código do idioma para a síntese de voz.
        genero_voz (google.cloud.texttospeech.SsmlVoiceGender): Gênero da voz (NEUTRAL, MALE, FEMALE).

    Returns:
        bytes: Áudio no formato MP3.
    """

    # Cliente da API do Google Text-to-Speech
    cliente = texttospeech.TextToSpeechClient()

    # Configuração da solicitação de síntese de voz
    entrada_sintese = texttospeech.SynthesisInput(text=texto)
    voz = texttospeech.VoiceSelectionParams(
        language_code=idioma,
        ssml_gender=genero_voz
    )
    config_audio = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Solicitação para a API
    resposta = cliente.synthesize_speech(
        input=entrada_sintese, 
        voice=voz, 
        audio_config=config_audio
    )

    # Retorna o áudio em bytes
    return resposta.audio_content

def salvar_audio(audio_bytes, caminho_arquivo):
    """
    Salva o áudio em um arquivo.

    Args:
        audio_bytes (bytes): Bytes do áudio a ser salvo.
        caminho_arquivo (str): Caminho para salvar o arquivo de áudio.
    """
    with open(caminho_arquivo, "wb") as out:
        out.write(audio_bytes)

# Exemplo de uso
if __name__ == "__main__":
    texto_para_sintetizar = "Olá, bem-vindo ao assistente de SQL IA."
    audio_bytes = sintetizar_voz_google(texto_para_sintetizar)
    salvar_audio(audio_bytes, "saida_audio.mp3")

