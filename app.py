import streamlit as st

# Inicializa variáveis de controle
if "questao" not in st.session_state:
    st.session_state.questao = 1
if "acertou" not in st.session_state:
    st.session_state.acertou = False

# Função para avançar fase
def avancar_fase():
    st.session_state.questao += 1
    st.session_state.acertou = False
    st.rerun()

# Perguntas
perguntas = {
    1: {
        "titulo": "FASE 1: CONHECIMENTO GERAL",
        "pergunta": "Qual é a principal forma de proteção da Ilha do Campeche?",
        "opcoes": [
            "A) É um Parque Nacional.",
            "B) É uma Área de Proteção Ambiental (APA).",
            "C) É uma Reserva Biológica.",
            "D) É um Sítio do Patrimônio Mundial da UNESCO."
        ],
        "correta": "B) É uma Área de Proteção Ambiental (APA)."
    },
    2: {
        "titulo": "FASE 2: REGRAS DE VISITAÇÃO",
        "pergunta": "Para manter a preservação, qual das seguintes regras de visitação é VERDADEIRA?",
        "opcoes": [
            "A) É permitido acampar com autorização prévia.",
            "B) É proibido o uso de protetor solar biodegradável.",
            "C) É permitido levar animais de estimação, desde que fiquem na coleira.",
            "D) O número de visitantes por dia é limitado para minimizar o impacto ambiental."
        ],
        "correta": "D) O número de visitantes por dia é limitado para minimizar o impacto ambiental."
    },
    3: {
        "titulo": "FASE 3: BIODIVERSIDADE",
        "pergunta": "Qual das seguintes espécies é Nativa da Ilha do Campeche?",
        "opcoes": [
            "A) Arara Azul.",
            "B) Tatu-bola.",
            "C) Mico-leão-dourado.",
            "D) Onça-pintada."
        ],
        "correta": "B) Tatu-bola."
    }
}

# Cabeçalho
with st.container(horizontal_alignment='center'):
    st.text("BEM-VINDO AO SHOW DA GOVERNANÇA DA ILHA DO CAMPECHE!")

fase = st.session_state.questao

if fase in perguntas:
    q = perguntas[fase]

    with st.container(border=True):
        with st.container(border=False, horizontal_alignment='center'):
            st.markdown(
                f"<h2 style='text-align: center;'>{q['titulo']}</h2>",
                unsafe_allow_html=True
            )
        st.markdown(q["pergunta"])

        resposta = st.radio(
            "Escolha a alternativa correta:",
            q["opcoes"],
            key=f"pergunta_{fase}",
            index=None
        )

        if st.button("Confirmar", key=f"responder_{fase}", type="primary", width="stretch"):
            if resposta == q["correta"]:
                st.session_state.acertou = True
                st.rerun()
            else:
                st.error("Resposta incorreta. Tente novamente.")

    # Se acertou, mostra botão de avançar
    if st.session_state.acertou:
        st.success("MAOEE Certa a resposta")
        st.balloons()
        with st.container(horizontal_alignment='right'):
            if st.button("Avançar agora ➡️", key=f"avancar_{fase}"):
                avancar_fase()

else:
    st.header("Parabéns! Você completou o Show da Governança da Ilha do Campeche!", anchor=False)
    st.text("Obrigado por participar e aprender sobre a importância da preservação ambiental. 🌱")
