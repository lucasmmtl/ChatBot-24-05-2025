🤖 Chatbot Zé Bonitinho 🥴
Este projeto tem como objetivo ensinar como construir um chatbot utilizando Python, Streamlit e a API da OpenAI. O bot, carinhosamente apelidado de "Zé Bonitinho 🥴",
assume a personalidade de um soldado da mais alta patente do exército brasileiro: rígido, direto e objetivo, com foco em disciplina e honra.

📚 Objetivo da Aula
Aprender como integrar a API da OpenAI em uma aplicação Python.

Construir uma interface web simples usando Streamlit.

Definir personalidades para chatbots por meio de instruções de sistema (system prompts).

Explorar conceitos de sessões, estado e interatividade em aplicações web.

🚀 Tecnologias Utilizadas
Python

Streamlit

OpenAI API (ChatGPT)

🛠️ Instalação e Execução
1. Clone este repositório:

git clone https://github.com/seuusuario/chatbot-ze-bonitinho.git
cd chatbot-ze-bonitinho

2. Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Configure sua chave da OpenAI:

[general]
OPENAI_API_KEY = "sua-chave-aqui"

5. Execute o aplicativo:

streamlit run "nomeDoArquivo.py"

🧠 Funcionamento do Chatbot
O bot carrega uma personalidade específica definida pelas instruções no código:

instructions_one = "Você é um soldado da mais alta patente do exército brasileiro. Deve ser rígido, direto e objetivo. Deve ensinar os usuários a como seguir uma vida correta, respeitada, honrada e com disciplina."

instructions_two = "Você deve evitar xingamentos pesados, pode pegar pesado com os usuários, mas sem os ofender diretamente, ou a sua família. Seja um líder e um exemplo a ser seguido."

O usuário interage via interface web.

O chatbot responde baseado nas mensagens anteriores, mantendo o contexto da conversa.

🔑 Estrutura do Código
app.py: Código principal do chatbot.

.streamlit/secrets.toml: Arquivo onde fica armazenada a chave da API (não subir no GitHub!).

requirements.txt: Dependências do projeto.

📝 Exemplo de Uso

Ao iniciar o aplicativo, você verá uma interface simples no navegador com um campo para perguntar algo. O chatbot irá responder de maneira direta, simulando um líder militar.

⚠️ Observações Importantes
A API da OpenAI é paga, com uma cota gratuita limitada. Consulte os preços em OpenAI Pricing.

Nunca compartilhe sua chave da OpenAI publicamente.

Este projeto é didático, use com responsabilidade.

🧑‍💻 Autor
Lucas Matheus
📅 24/05/2025

⚖️ Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

