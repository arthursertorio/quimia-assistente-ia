import json
import os
import streamlit as st
from openai import OpenAI


# ==========================================
# CONFIGURAÇÃO
# ==========================================

st.set_page_config(
    page_title="QuimIA",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 QuimIA")
st.subheader("Assistente de Estudos para Engenharia Química")


# ==========================================
# CARREGAR BASE DE CONHECIMENTO
# ==========================================

BASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "base_conhecimento.json"
)

with open(BASE_PATH, "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)


def criar_contexto(base):

    contexto = ""

    for disciplina in base["disciplinas"]:

        contexto += f"\nDISCIPLINA: {disciplina['nome']}\n"

        for topico in disciplina["topicos"]:

            contexto += f"""
TÓPICO: {topico['titulo']}
CONTEÚDO: {topico['conteudo']}
"""

    return contexto


contexto = criar_contexto(base)


# ==========================================
# API
# ==========================================

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:

    st.error(
        "A variável OPENAI_API_KEY não foi configurada."
    )

    st.stop()


client = OpenAI(
    api_key=api_key
)


# ==========================================
# PROMPT
# ==========================================

SYSTEM_PROMPT = f"""
Você é o QuimIA, um assistente educacional para estudantes
de Engenharia Química.

Use a base de conhecimento abaixo para responder.

REGRAS:

- Seja claro e didático.
- Explique passo a passo quando necessário.
- Não invente informações.
- Se a resposta não estiver na base, diga que não possui
  informação suficiente.
- Não apresente informações incertas como fatos.
- Sugira um próximo passo de estudo.

BASE DE CONHECIMENTO:

{contexto}
"""


# ==========================================
# HISTÓRICO
# ==========================================

if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )


# ==========================================
# CHAT
# ==========================================

pergunta = st.chat_input(
    "Digite sua dúvida de Engenharia Química..."
)


if pergunta:

    st.session_state.messages.append({

        "role": "user",

        "content": pergunta

    })

    with st.chat_message("user"):

        st.markdown(pergunta)


    mensagens = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ]

    mensagens.extend(
        st.session_state.messages
    )


    with st.chat_message("assistant"):

        with st.spinner("Pensando..."):

            resposta = client.chat.completions.create(

                model="gpt-4o-mini",

                messages=mensagens,

                temperature=0.2

            )

            texto = (
                resposta
                .choices[0]
                .message
                .content
            )

            st.markdown(texto)


    st.session_state.messages.append({

        "role": "assistant",

        "content": texto

    })
