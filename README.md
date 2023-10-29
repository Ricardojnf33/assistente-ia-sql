# ai_sql_shop_assistent
Um bot assistente que realiza uma query a uma Base de Dados vectorizadas

projeto_sql_ia/
├── streamlit_app.py # arquivo principal da aplicação Streamlit
├── requerimentos.txt # bibliotecas requeridas
├── prompts/ 
|   └── prompt.yml # arquivo com o prompt GPT
├── imagens/
|   └── erd.png # imagem do diagrama ERD
├── sql_exec.py # função para executar query no banco
├── app_secrets.py # arquivo com chaves de API

O arquivo streamlit_app.py contém o código principal da aplicação, incluindo:

Importação de bibliotecas
Layout do app Streamlit
Carregamento do prompt GPT
Integração com GPT e banco de dados
Exibição dos resultados
O arquivo prompt.yml contém o prompt/template usado para treinar o modelo GPT.

O arquivo sql_exec.py contém a função para se conectar ao banco Snowflake e executar as queries SQL geradas pelo GPT.

O arquivo app_secrets.py contém tokens e chaves que não devem ser versionados, como a chave de API do OpenAI.

A pasta imagens contém os assets usados no app, como o diagrama ERD.

E a pasta prompts agrupa diferentes versões dos prompts usados para treinar o GPT.

Assim fica mais organizado e with descrição do papel de cada arquivo/pasta no projeto. 
