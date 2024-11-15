import streamlit as st
# Bibliotecas necessárias para comunicação com servidor OPC UA
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

user = st.session_state["name"]
user = str(user)

with st.sidebar:
    st.write('Olá, ' + user.rsplit(' ')[0] + "!")

authenticator.logout("Sair", "sidebar")

conn = st.connection('mysql', type='sql') # C:\Users\Rafael\.streamlit\secrets.toml
url = "opc.tcp://127.0.0.1:4840/"

st.title("Painel de Controle")

tab1, tab2 = st.tabs(["Posição", "Velocidade"])

dv_True = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))  # data value True
dv_False = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean))  # data value False

placeholder = st.empty() # Container for position display
placeholder2 = st.empty()

async def main():
   async with Client(url=url) as client:     
    node_power = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.Power")
    node_power_on = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.PowerOn")
    node_pos = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Position")
    node_mov_vel = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveVelocity")
    node_mov_abs = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveAbsolute")
    node_ac = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Acceleration")
    node_dac = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Deceleration")
    node_vel = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Velocity")
    node_direction = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Direction")
    node_error = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.Error")

    c1, c2 = st.columns(2)

    error = await node_error.read_value()

    with c1:
        motor_on_off = st.toggle("Ligar/Desligar Motor")   
        direcao = st.radio('Escolha o sentido de rotação:', ["Sentido Horário", "Sentido Anti-horário", "Caminho mais curto"],captions= ["","","Apenas para controle de posição"])
    with c2:
        if (motor_on_off and not error):
            st.image('images/motor_on.png',width=150)
        elif (not motor_on_off and not error):
            st.image('images/motor_off.png',width=150)
        elif (error):
            st.image('images/motor_error.png',width=150)    

    if (direcao == "Sentido Horário"):
        await node_mov_abs.write_value(dv_False)
        dv = ua.DataValue(ua.Variant(0, ua.VariantType.Int32))  # data value
        await node_direction.write_value(dv)

    elif(direcao == "Sentido Anti-horário"):
        await node_mov_abs.write_value(dv_False)
        dv = ua.DataValue(ua.Variant(1, ua.VariantType.Int32))  # data value
        await node_direction.write_value(dv) 

    else:
        await node_mov_abs.write_value(dv_False)
        dv = ua.DataValue(ua.Variant(3, ua.VariantType.Int32))  # data value
        await node_direction.write_value(dv) 

    if motor_on_off:
        st.write(":gear: Motor Ligado!")
        await node_power.write_value(dv_True)
    else:
        st.write(":warning: Motor Desligado!")
        await node_mov_abs.write_value(dv_False)
        await node_power.write_value(dv_False)
    
    with tab1:   
        if(await node_vel.read_value() == 0.00 or await node_ac.read_value() == 0.00 or await node_dac.read_value() == 0.00):
            st.warning(":heavy_exclamation_mark: Configure a velocidade!")

        pos = 0.0
        pos = st.slider('Posição', 0.00, 359.99, pos, 0.50)

        start_pos = st.button("Posicionar Eixo",key="Ligar Controle de Posição")
        if(start_pos):
            if not motor_on_off:
                st.warning(":heavy_exclamation_mark: Ligue o motor para iniciar o teste!")
            else:   
                dv = ua.DataValue(ua.Variant(pos, ua.VariantType.Double))  # data value
                await node_pos.write_value(dv)
                # Checar se motor está ligado
                if (not await node_power_on.read_value()):
                    await node_mov_abs.write_value(dv_False)
                    await node_mov_vel.write_value(dv_False)
                elif (await node_power_on.read_value() and not await node_mov_vel.read_value()):
                    await node_mov_abs.write_value(dv_True)      
                    
    with tab2:
        # Sliders
        ac = 0.00
        ac = st.slider('Aceleração', 0.00, 3600.00, ac, 0.50)

        dac = 0.00
        dac = st.slider('Desaceleração', 0.00, 3600.00, dac, 0.50)

        vel = 0.00
        vel = st.slider('Velocidade', 0.00, 3600.00, vel, 0.50)

        dv = ua.DataValue(ua.Variant(ac, ua.VariantType.Float))  # data value
        await node_ac.write_value(dv)

        dv = ua.DataValue(ua.Variant(dac, ua.VariantType.Float))  # data value
        await node_dac.write_value(dv)

        dv = ua.DataValue(ua.Variant(vel, ua.VariantType.Float))  # data value
        await node_vel.write_value(dv)

        columns = st.columns([1, 1, 1, 1, 1, 1, 1])
        with columns[0]:
            start_vel = st.button(':arrow_forward: Acionar Motor',key="Ligar Controle de Velocidade")
        with columns[1]:
            stop_vel = st.button(':white_medium_square: Parar Motor',key="Desligar Controle de Velocidade")
        
        if start_vel:
            if(not await node_power_on.read_value()):
                st.warning(":heavy_exclamation_mark: Ligue o motor para iniciar o teste!")
            elif(await node_vel.read_value() == 0.00 or await node_ac.read_value() == 0.00 or await node_dac.read_value() == 0.00):
                st.warning(":heavy_exclamation_mark: Configure a velocidade!")    
            elif(direcao == "Caminho mais curto"):
                st.warning(":heavy_exclamation_mark: Configure o sentido de rotação!")  
            else:    
                await node_mov_abs.write_value(dv_False)
                await node_mov_vel.write_value(dv_True)    
                
        if stop_vel:
            await node_mov_abs.write_value(dv_False)
            if(not await node_power_on.read_value()):
                st.warning(":heavy_exclamation_mark: Ligue o motor para iniciar o teste!")
            else:
                await node_mov_vel.write_value(dv_False)
                await node_mov_abs.write_value(dv_False) 
        
        while motor_on_off:
            with placeholder.container():
                    df = conn.query('SELECT Position FROM análise ORDER BY Time DESC LIMIT 1', ttl=1) # takes the last position recorded to show
                    st.metric("Posição atual", df['Position'])  

if __name__ == "__main__":
    user = st.session_state["username"]
    role = config["credentials"]["usernames"][user]["role"]

    if role != "Professor Orientador":
        st.header('Desculpe, mas você não tem permissão para acessar esta página :(')
    else:
        asyncio.run(main())