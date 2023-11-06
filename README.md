# Assistente SQL com IA
Este projeto consiste em um assistente de SQL com IA para consultas em banco de dados Snowflake. O assistente recebe uma pergunta em linguagem natural do usuário e gera a consulta SQL correspondente.

## Funcionamento
O fluxo do assistente é:

1. O usuário insere uma pergunta em linguagem natural na interface
2. A pergunta é passada para a cadeia de geração de linguagem LangChain
3. LangChain usa o modelo de linguagem GPT-3 da Anthropic para gerar a query SQL correspondente
4. A consulta SQL é executada no Snowflake usando a biblioteca Python snowflake-connector
5. O resultado da consulta é exibido na interface para o usuário


A interface foi construída com Streamlit e o aplicativo roda localmente.

**Tecnologias**

As principais tecnologias usadas no projeto:

* LangChain para geração de linguagem
* GPT-3 da Anthropic como LLM
* Snowflake para banco de dados em nuvem
* Streamlit para interface web

**Estrutura de Arquivos** 

* images/: contém diagrama ERD
* prompts/: contém o template de prompt usado no LangChain
* pycache/: cache Python
* README.md: este arquivo
* demo.py: script principal com interface Streamlit
* requirements.txt: dependencies do projeto
* sql_execution.py: funções para executar queries SQL no Snowflake

**Como Usar**

Pré-requisitos

* Python 3.7+
* Conta na OpenAI
* Conta Snowflake

**Passos**

1. Clone este repositório
2. Instale as dependências com pip install -r requirements.txt
3. Configure as credenciais Snowflake e chave API Anthropic em app_secrets.py
4. Execute streamlit run demo.py
5. Insira uma pergunta na caixa de texto e clique Enter

Exemplo

Pergunta:

Quais o total de lojas do shopping?


