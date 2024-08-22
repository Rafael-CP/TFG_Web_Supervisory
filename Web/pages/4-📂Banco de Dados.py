import streamlit as st
# Bibliotecas necessárias para comunicação com servidor OPC UA
import asyncio
import pandas as pd # Gerenciamento de dataframes
from datetime import date, time
from asyncua import *
from opcua import ua
from sqlalchemy import * # Comunicação com o banco de dados
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

if st.session_state["authentication_status"] is None:
    st.switch_page("🔐Login.py")  

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.logout("Sair", "sidebar")

st.sidebar.markdown("""
    <style>

        [data-testid="stSidebarNav"]::before {
            content: "Supervisório Web";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 25px;
            position: relative;
            top: 0px;
        }
    </style>           
                    
    <style>
    [data-testid='stSidebarNav'] > ul {
        min-height: 65vh;
    } 
    </style>
                    
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

url = "opc.tcp://127.0.0.1:4840/"
conn = st.connection('mysql', type='sql') # C:\Users\Rafael\.streamlit\secrets.toml

st.title("Consulta ao Banco de Dados")
async def main():
   async with Client(url=url) as client:
        
    opcao_db = st.selectbox("Selecione o Banco de Dados a ser analisado", ("Parâmetros", "Comando", "Análise", "Status"))

    # Adicionar seletor de dias do mes https://docs.streamlit.io/develop/api-reference/widgets/st.date_input
    date_db = st.date_input("Data")

    # Seletor de quantidade de dados a serem exibidos na tabela.
    num_db = st.slider("Escolha o período dos dados que deseja analisar", value=(time(12, 00), time(13, 00)))

    query_db = 'SELECT * FROM %s WHERE TIME BETWEEN "%s" AND "%s"' % (opcao_db, str(date_db) + " " + str(num_db[0].hour) + ":" + str(num_db[0].minute), (str(date_db)) + " " + str(num_db[1].hour) + ":" + str(num_db[1].minute))
    
    df = conn.query(query_db, ttl=0)
    st.dataframe(df, hide_index=True)

if __name__ == "__main__":

    asyncio.run(main())