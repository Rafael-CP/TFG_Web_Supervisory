import streamlit as st
import asyncio
from asyncua import *
from opcua import ua
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

st.title("Página de Alarmes")

conn = st.connection('mysql', type='sql') # C:\Users\Rafael\.streamlit\secrets.toml
url = "opc.tcp://127.0.0.1:4840/"

placeholder = st.empty()

dv_True = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))  # data value True
dv_False = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean))  # data value False

async def main():
    async with Client(url=url) as client:  
        node_power = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.Power")
        node_mov_vel = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveVelocity")
        node_mov_abs = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveAbsolute")
        node_mov_add = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveAdditive")
        node_error_reset = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.ErrorReset")
        node_home = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.Home")
        alarm1_ack = client.get_node("ns=6;s=::AsGlobalPV:Alarm1.Acknowledgement")

        query_db = 'SELECT * FROM Alarmes ORDER BY Time DESC LIMIT 5' 
    
        df = conn.query(query_db, ttl=0)
        st.data_editor(df,  
            column_config={
                "Reconhecimento": st.column_config.CheckboxColumn(
                "Reconhecido?",
                default=False,
                )
            },
        disabled=["widgets"],
        hide_index=True,
        )

        error_reset = st.button(":broom: Resetar Estado de Erro", key = 'erro')

        if error_reset:
            await node_error_reset.write_value(dv_True)
            await asyncio.sleep(0.5)
            await node_error_reset.write_value(dv_False)

        reset_all = st.button(":arrows_counterclockwise: Resetar todas as variáveis", key = 'reset_all')

        if reset_all:
            await node_power.write_value(dv_False)
            await node_mov_vel.write_value(dv_False)
            await node_mov_abs.write_value(dv_False)
            await node_mov_add.write_value(dv_False)
            await node_home.write_value(dv_True)
            await asyncio.sleep(0.5)
            await node_home.write_value(dv_False)

        alarm_ack = st.button(":no_bell: Reconhecer Alarmes",key = 'ack_all')

        if alarm_ack:
            await alarm1_ack.write_value(dv_True)
            await asyncio.sleep(0.5)
            await alarm1_ack.write_value(dv_False)

        
if __name__ == "__main__":
    asyncio.run(main())