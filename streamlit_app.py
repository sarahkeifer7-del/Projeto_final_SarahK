import streamlit as st
from datetime import datetime
# Importação do Firebase/Firestore
# Se não estiver usando, comente ou remova as linhas relacionadas ao firestore
from google.cloud import firestore


# Configuração da conexão com o Firestore (Manter se for usar)
# Assumindo que você tem o arquivo 'firebase.json' e a biblioteca instalada.
try:
   db = firestore.Client.from_service_account_json("firebase.json")
except Exception as e:
   st.error(f"Erro ao conectar ao Firestore: {e}. Certifique-se de que 'firebase.json' está correto.")
   db = None # Define como None se a conexão falhar


# --- Configuração da Página ---
st.set_page_config(
    page_title="Universo em Foco",
    page_icon="🌌",
    layout="wide"
)
st.markdown("""
<style>

/* Fundo principal */
.stApp {
    background: linear-gradient(
        135deg,
        #071629,
        #101c3a,
        #24143b
    );
    color: #F4F7FB;
}

/* Títulos */
h1, h2, h3 {
    color: #EAF6FF;
}

/* Botões */
.stButton > button {
    background-color: #49256B;
    color: white;
    border: 1px solid #83D8FF;
    border-radius: 12px;
    padding: 8px 20px;
}

/* Efeito ao passar o mouse */
.stButton > button:hover {
    background-color: #65408A;
    border-color: #83D8FF;
    color: white;
}
/* Melhorar a leitura do menu */
.stRadio label,
.stRadio label p {
    color: #EAF6FF !important;
}

/* Melhorar os textos dos campos */
.stTextInput label,
.stTextArea label {
    color: #EAF6FF !important;
}
/* Personalização dos cartões dos artigos */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: rgba(16, 28, 58, 0.85);
    border: 1px solid #35527a;
    border-radius: 18px;
    padding: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: border-color 0.3s ease;
}

/* Efeito ao passar o mouse */
div[data-testid="stVerticalBlockBorderWrapper"]:hover,
div[data-testid="stVerticalBlockBorderWrapper"]:hover > div {
    border-color: #83D8FF !important;
    box-shadow: 0 0 14px rgba(131, 216, 255, 0.25);
}
/* Campos de nome, e-mail e mensagem */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    background-color: #101c3a !important;
    color: #EAF6FF !important;
    -webkit-text-fill-color: #EAF6FF !important;
    caret-color: #83D8FF !important;
    border: 1px solid #35527a !important;
    border-radius: 10px !important;
}

/* Texto de orientação dos campos */
div[data-testid="stTextInput"] input::placeholder,
div[data-testid="stTextArea"] textarea::placeholder {
    color: #AABBD0 !important;
    -webkit-text-fill-color: #AABBD0 !important;
}

/* Destaque ao selecionar um campo */
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border: 1px solid #83D8FF !important;
}

/* Botão de envio */
div[data-testid="stFormSubmitButton"] button {
    background-color: #49256B !important;
    color: white !important;
    -webkit-text-fill-color: white !important;
    border: 1px solid #83D8FF !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# --- Dados Mock (Posts de Exemplo) ---
# Use links de imagem placeholder
PLACEHOLDER_IMAGE_URL_1 = "https://via.placeholder.com/770x300?text=Imagem+do+Post+Recente+1"
PLACEHOLDER_IMAGE_URL_2 = "https://via.placeholder.com/770x300?text=Imagem+do+Post+Recente+2"
PLACEHOLDER_AVATAR_URL = "https://via.placeholder.com/150?text=Avatar"


POSTS = [
      {
        "id": 1,
        "title": "Conhecendo o Sistema Solar",
        "author": "Equipe Universo em Foco",
        "date": "2026-11-07",
        "summary": "O Sistema Solar é formado pelo Sol e pelos corpos celestes que orbitam ao seu redor. Conheça os oito planetas e descubra algumas curiosidades sobre nossa vizinhança espacial!",
        "image": "https://assets.science.nasa.gov/dynamicimage/assets/science/psd/solar/2023/10/planets3x3_pluto_colorMercury_axis_tilt_1080p.00001_print-1.jpg?format=jpeg&w=4096",
    },
    {
        "id": 2,
        "title": "Os mistérios da Lua",
        "author": "Equipe Universo em Foco",
        "date": "2026-11-07",
        "summary": "A Lua é o satélite natural da Terra. Suas diferentes fases acontecem conforme observamos diferentes partes de sua superfície iluminada pelo Sol.",
        "image": "https://assets.science.nasa.gov/dynamicimage/assets/science/psd/lunar-science/2023/08/lro_fullmoon.jpg?crop=faces%2Cfocalpoint&fit=clip&h=3240&w=3240",
    },
    {
        "id": 3,
        "title": "O que são as galáxias?",
        "author": "Equipe Universo em Foco",
        "date": "2026-11-07",
        "summary": "Galáxias são enormes estruturas formadas por estrelas, planetas, gás e poeira. Nossa casa no universo é a Via Láctea!",
        "image": "https://assets.science.nasa.gov/dynamicimage/assets/science/astro/universe/homepage-updates/NGC-6357.jpg?crop=faces%2Cfocalpoint&fit=clip&format=jpeg&w=2560",
    },
]
   # Adicione mais posts conforme necessário


# --- Funções Auxiliares ---


def render_post_card(post):
    with st.container(border=True):

        col_img, col_text = st.columns([1, 2])

        with col_img:
            st.image(
                post["image"],
                use_container_width=True
            )

        with col_text:
            st.markdown(f"### {post['title']}")

            st.caption(
                f"Por {post['author']} • {post['date']}"
            )

            st.write(post["summary"])

            st.markdown("✨ Universo em Foco")

# --- Layout e Interatividade ---


# O toggle de tema nativo do Streamlit é geralmente preferido.
# Se você quiser um toggle customizado, você precisará de CSS mais robusto.
# O código de aplicação de CSS para tema foi removido, pois o tema nativo
# do Streamlit pode ser controlado nas configurações.
# O toggle abaixo apenas demonstra um widget:


# Exemplo de um toggle (você pode usá-lo para controlar outras cores customizadas)
st.toggle("Tema Customizado", value=False)


# --- Barra Superior / Hero Section ---
imagem_banner = "https://assets.science.nasa.gov/dynamicimage/assets/science/astro/exo-explore/internal_resources/1763/image_of_nebula_W51.jpeg?crop=faces%2Cfocalpoint&fit=clip&h=900&w=1600"

banner_html = """
<div style="
    width: 100%;
    height: 280px;
    background-image:
        linear-gradient(rgba(7,22,41,0.25), rgba(7,22,41,0.25)),
        url('URL_DA_IMAGEM');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    border-radius: 18px;
">
</div>
"""

st.markdown(
    banner_html.replace("URL_DA_IMAGEM", imagem_banner),
    unsafe_allow_html=True
)
st.title("🌌 Universo em Foco")

st.markdown(
    "### Explorando os mistérios do universo, "
    "uma descoberta de cada vez."
)

st.caption("ASTRONOMIA • CIÊNCIA • DESCOBERTAS")

st.markdown("---")


# --- Seção Principal + Barra Lateral ---
main, sidebar = st.columns([3, 1])


with sidebar:
   st.header("Navegação 🧭")
   # Define a página inicial
   page = st.radio("Ir para", ["Início", "Sobre", "Contato"])
  
   st.header("Pesquisar 🔍")
   query = st.text_input("Buscar por título ou autor")
  
   st.markdown("---")
   st.write("Siga nas redes:")
   st.write("• X / Twitter: @seuperfil")
   st.write("• LinkedIn: /seuperfil")


with main:
   if page == "Início":
       st.header("Posts Recentes ✨")


       # Filtro de pesquisa simples
       filtered = POSTS
       if query:
           q = query.lower()
           filtered = [p for p in POSTS if q in p['title'].lower() or q in p['author'].lower()]


       if filtered:
           for post in filtered:
               with st.container():
                   render_post_card(post)
                   st.markdown("---")
       else:
            st.info("Nenhum post encontrado com o critério de pesquisa.")


   elif page == "Sobre":
        st.header("Sobre o Universo em Foco 🌌")

        st.write(
            "O Universo em Foco é um website educativo dedicado "
            "à astronomia e à exploração dos mistérios do universo."
        )

        st.subheader("Nossa proposta 🔭")

        st.write(
            "Nosso objetivo é compartilhar conhecimentos sobre o espaço, "
            "apresentando informações de maneira simples, visual e acessível."
        )

        st.subheader("O que você encontrará aqui? 🪐")

        st.markdown("""
        - **Sistema Solar:** conheça os planetas e outros corpos celestes.
        - **Lua:** descubra suas fases e características.
        - **Galáxias:** explore as enormes estruturas que formam o universo.
        """)

        st.subheader("Nosso objetivo ✨")

        st.write(
            "Queremos despertar a curiosidade científica dos visitantes "
            "e tornar o aprendizado sobre astronomia mais interessante."
        )

   elif page == "Contato":
        st.header("💌 Entre em contato")

        st.write(
            "Tem alguma dúvida, sugestão ou curiosidade sobre astronomia? "
            "Adoraríamos receber sua mensagem!"
         )

        st.caption(
            "Preencha os campos abaixo para conversar com a equipe Universo em Foco."
         )


        with st.form("fale_conosco"):

            st.subheader("Envie sua mensagem ✨")

            name = st.text_input(
                "Seu nome",
                placeholder="Digite seu nome"
            )

            email = st.text_input(
                "Seu e-mail",
                placeholder="exemplo@email.com"
            )

            message = st.text_area(
                "Sua mensagem",
                placeholder="Escreva sua mensagem aqui..."
            )

            if st.form_submit_button("Enviar mensagem 🚀"):

                if not name or not email or not message:
                    st.warning("Preencha todos os campos antes de enviar.")

                elif db is None:
                    st.error(
                        "A conexão com o Firestore falhou. "
                        "Verifique a configuração do Firebase."
                    )

                else:
                    try:
                        novo_documento = db.collection(
                            "contato_mensagem"
                        ).document()

                        novo_documento.set(
                            {
                                "name": name,
                                "email": email,
                                "message": message,
                                "timestamp": datetime.now()
                            }
                        )

                        st.success(
                            "Obrigado! Sua mensagem foi enviada! 💙"
                        )

                    except Exception as e:
                        st.error(
                            "Erro ao salvar mensagem no Firestore: {e}"
                        )

# --- Rodapé (Footer) ---
st.markdown("---")
colf1, colf2 = st.columns([1, 3])
with colf1:
   st.write(f"© {datetime.now().year} Nome do Seu Blog")
with colf2:
   st.write("Template de exemplo para Streamlit — personalize cores, fontes e layout conforme a necessidade.")

