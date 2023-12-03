Configuração do Ambiente
Instalar Dependências:

Execute pip install -r requirements.txt para instalar todas as dependências necessárias.
Variáveis de Ambiente:

Defina as seguintes variáveis de ambiente no arquivo .env:
OPENAI_API_KEY: Sua chave de API para o OpenAI.
GOOGLE_APPLICATION_CREDENTIALS: Caminho para sua chave de API do Google Cloud (para TTS).
Variáveis para a conexão Snowflake (SF_USER, SF_PASSWORD, etc.).
Uso do Aplicativo
Executar o demo.py:

Inicie o aplicativo com streamlit run demo.py.
Acesse a interface do usuário via navegador conforme indicado pelo Streamlit.
Interagir com a Aplicação:

Digite sua consulta na caixa de texto.
Visualize o resultado da consulta SQL, o texto da consulta e o diagrama ERD.
Utilize a funcionalidade de síntese de voz, se necessário.
Configuração da Síntese de Voz
Google Text-to-Speech:
Siga as instruções da Google Cloud para configurar a API Text-to-Speech.
Certifique-se de que a chave da API esteja corretamente configurada no .env.
Manutenção e Suporte
Para problemas, dúvidas ou contribuições, por favor, abra uma issue no repositório do GitHub ou entre em contato com os mantenedores do projeto.


Qual o total de lojas do shopping?

![Exemplo Query](https://github.com/<seu_usuario>/<seu_repo>/blob/main/images/Exemplo_query.png.png?raw=true)
