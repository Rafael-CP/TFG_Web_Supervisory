# Autenticação:
import streamlit as st # Desenvolvimento de Aplicação Web
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title='Login', page_icon=':robot_face:', layout='wide',initial_sidebar_state="collapsed")
st.title("Página Inicial - Autenticação")
# Escondendo barra de navegação e botão de fullscreen das imagens com CSS
st.markdown( 
    """
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>

<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Centralizando imagem: 5 colunas e a imagem na coluna central
l1, l2, l3, l4, l5, center, r1, r2, r3, r4, r5 = st.columns(11)
with l5:
    st.image('images/UNIFEI.png',width=250)

st.write('Bem-vindo ao Sistema Supervisório Web!')

# Autenticação de Usuário
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
if st.session_state["authentication_status"] is None:
    st.warning(':old_key: Por favor informe Usuário e Senha')

name, authentication_status, username = authenticator.login(fields = {'Form name':'Entrar no Sistema', 'Username':'Usuário', 'Password':'Senha','Login':'Entrar'})

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.switch_page("pages/1-📈Dashboard.py")    
elif st.session_state["authentication_status"] is False:
    st.error('Usuário ou Senha inválido!')