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
        "titulo": "MÀ OE! Bem vindo ao Show Da Governança",
        "pergunta": "Vamos a primeira pergunta:O que é a governança pública?",
        "opcoes": [
            "A) Conjunto de instituições que atuam de forma independente na gestão de um bem público",
            "B) Sistema de regras, princípios e mecanismos de gestão e controle para tomar decisões de forma ética, responsável e transparente, visando alcançar objetivos coletivos e atender ao interesse público",
            "C) Sistema de regras que visa interesses particulares por meio da exploração de um bem público",
            "D) Forma de governo em que apenas líderes políticos tomam todas as decisões sem participação social"
        ],
        "correta": "B) Sistema de regras, princípios e mecanismos de gestão e controle para tomar decisões de forma ética, responsável e transparente, visando alcançar objetivos coletivos e atender ao interesse público"
    },
    2: {
        "titulo": "Muito bem! Vamos a proxima pergunta",
        "pergunta": "Quais áreas a governança pública eficaz deve abranger?",
        "opcoes": [
            "A) Social, Econômica e Ambiental",
            "B) Iniciativa privada, Lucratividade",
            "C) Orçamento participativo, Hierarquia de cargos",
            "D) Esportiva, Religiosa e Militar"
        ],
        "correta": "A) Social, Econômica e Ambiental"
    },
    3: {
        "titulo": "Má oe, ma vem pra cá",
        "pergunta": "Proxima pergunta: A governança pública deve garantir:",
        "opcoes": [
            "A) Segurança, Benefícios individuais, Conservação",
            "B) Investimentos, Desvio de recursos, Integridade pública",
            "C) Transparência, prestação de contas, equidade e responsabilidade",
            "D) Sigilo total das informações públicas"
        ],
        "correta": "C) Transparência, prestação de contas, equidade e responsabilidade"
    },
     4: {
        "titulo": "vem pra cá vem pra cá",
        "pergunta": "Proxima pergunta: A Ilha do Campeche foi tombada em qual ano?",
        "opcoes": [
            "A) 1974",
            "B) 1995",
            "C) 2000",
            "D) 1988"
        ],
        "correta": "C) 2000"
    },
      5: {
        "titulo": "É com você, Lombardi!",
        "pergunta": "Proxima pergunta: Segundo a legislação vigente o número de visitantes permitido por dia na Ilha do Campeche é de:",
        "opcoes": [
            "A) 2000 visitantes por dia",
            "B) 1200 visitantes por dia",
            "C) 800 visitantes por dia",
            "D) 500 visitantes por dia"
        ],
        "correta": "C) 800 visitantes por dia"
    },
    6: {
        "titulo": "Olha a Tele-Sena",
        "pergunta": "Proxima pergunta: Um dos principais desafios da governança na Ilha do Campeche é:",
        "opcoes": [
            "A) Manter o acesso, simplificando a fiscalização de transporte e ingressos",
            "B) Aumentar o número de visitantes para gerar mais renda para a comunidade local",
            "C) Equilibrar a conservação ambiental com o turismo sustentável",
            "D) Garantir a autoridade da comunidade local nas decisões"
        ],
        "correta": "C) Equilibrar a conservação ambiental com o turismo sustentável"
    },
    7: {
        "titulo": "Ultima pergunta, valendo um milhão de gerais",
        "pergunta": "A participação da comunidade na governança da Ilha do Campeche é importante porque...",
        "opcoes": [
            "A) Facilita a exploração sem regulamentação por parte de empresas privadas",
            "B) É irrelevante, pois somente órgãos federais decidem sobre o patrimônio",
            "C) Serve apenas para fins decorativos em reuniões públicas",
            "D) Garante que os interesses locais e o conhecimento tradicional sejam considerados na gestão"
        ],
        "correta": "D) Garante que os interesses locais e o conhecimento tradicional sejam considerados na gestão"
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