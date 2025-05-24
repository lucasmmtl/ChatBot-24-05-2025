import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

st.title("zé bonitinho 🥴")

if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-4o-mini'

if "messages" not in st.session_state:
    st.session_state['messages'] = [# {"role": "system", "content": "Você é um assistente útil."}
        ]
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

instructions_one = "Você é um soldado da mais alta patente do exército brasileiro. Deve ser rigido, direto e objetivo. Deve ensinar os usuários a como seguir uma vida correta, respeitada, honrada e com disciplica"
instructions_two = "Você deve evitar xingamentos pessados, pode pegar pesado com os usuários, mas sem os ofender diretamente, ou a sua família. Seja um lider e um exemplo a ser seguido"

if prompt := st.chat_input("Pergunte alguma coisa"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.spinner("Pensando..."):
        response = client.chat.completions.create(
            model=st.session_state['openai_model'],
            messages = [
            {"role": "system", "content": instructions_one},
            {"role": "system", "content": instructions_two},
            {"role": "user", "content": prompt}
        ],
            temperature=0.7,
            max_tokens=1000
        )
        bot_response = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.markdown(bot_response)

# if prompt := st.chat_input("Pergunte alguma coisa"):
#     instructions_one = "Você é um assistente virtual que ajuda os usuários a encontrar informações sobre produtos e serviços. Você deve ser amigável, prestativo e fornecer respostas claras e concisas."
#     instructions_two = "Você deve evitar dar conselhos médicos, legais ou financeiros. Se o usuário fizer uma pergunta sobre esses tópicos, você deve redirecioná-lo para um profissional qualificado."
    
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("usar"):
#         st.markdown(prompt)

# with st.chat_message("assistant"):
#     stream = client.chat.completions.creat(
#         model = st.session_state['openai_model'],
#         messages = [
#             {"role": "system", "content": instructions_one},
#             {"role": "system", "content": instructions_two},
#             {"role": "user", "content": prompt}
#         ],
#         stream = True,
#     )
#     response = st.write_stream(stream)

