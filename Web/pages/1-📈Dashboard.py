import streamlit as st # Desenvolvimento de Aplicação Web
import asyncio
from asyncua import *
from opcua import ua # MANTENHA O ARQUIVO opcua.py NO DIRETORIO DESTE PROGRAMA - MOTIVO DESCONHECIDO :)
from sqlalchemy import * # Comunicação com o banco de dados
import plotly.express as px # Plot de gráficos
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title='Dashboard', page_icon=':robot_face:', layout='wide')
st.title("Dashboard")
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

user = st.session_state["name"]
user = str(user)
st.write('Olá, ' + user + "!")

with st.sidebar:
    st.write('Olá, ' + user.rsplit(' ')[0] + "!")


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

conn = st.connection('mysql', type='sql') # C:\Users\Rafael\.streamlit\secrets.toml

# Endereço do servidor para conexão com o cliente OPC UA
url = "opc.tcp://127.0.0.1:4840/"

placeholder = st.empty()

dv_True = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))    # data value True
dv_False = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean))  # data value False

dv_distance = ua.DataValue(ua.Variant(10, ua.VariantType.Double))  
dv_param = ua.DataValue(ua.Variant(10, ua.VariantType.Float))

async def main():
    async with Client(url=url) as client:      
        node_mov_add = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveAdditive")
        node_distance = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Distance")
        node_power = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.Power")
        node_ac = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Acceleration")
        node_dac = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Deceleration")
        node_vel = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Velocity")
        node_home = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.Home")

        await node_ac.write_value(dv_param)
        await node_dac.write_value(dv_param)
        await node_vel.write_value(dv_param)
        await node_distance.write_value(dv_distance)

        st.write("Teste do motor - Avança 10 graus em sentido horário")
        pos_impulse = st.button("Posicionar Eixo",key="Ligar Controle de Posição")
        
        if pos_impulse:
            await node_power.write_value(dv_True)
            await node_home.write_value(dv_False)
            await asyncio.sleep(0.5)
            await node_mov_add.write_value(dv_True)
        else:   
            await node_home.write_value(dv_True)

        while(True):          
            with placeholder.container():
                df = conn.query('SELECT * FROM análise ORDER BY Time DESC LIMIT 100;', ttl=0) # TTL => muda a taxa de atualizacao do grafico

                col1, col2= st.columns(2)
                
                with col1:
                    fig = px.line(df, x=df["Time"], y=df["Position"], labels={"Position" : "Posição", "Time" : "Tempo"}, title="Posição do Eixo")
                    fig.update_layout({"uirevision": "foo"}, overwrite=True,width=600, title_x=0.5)
                    st.write(fig)

                with col2:
                    fig = px.line(df, x=df["Time"], y=df["Velocity"], labels={"Velocity" : "Velocidade", "Time" : "Tempo"}, title="Velocidade do Eixo")
                    fig.update_layout({"uirevision": "foo"}, overwrite=True,width=600, title_x=0.5)
                    st.write(fig)
            
if __name__ == "__main__":
  asyncio.run(main())