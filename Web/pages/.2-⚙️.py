import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import asyncio
from asyncua import *
from opcua import ua
import math

url = "opc.tcp://127.0.0.1:4840/"

dv_True = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))  # data value True
dv_False = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean))  # data value False

motor_on_off = st.toggle("Ligar/Desligar Motor")   

if st.session_state["authentication_status"] is None:
    st.switch_page("🔐Login.py")  

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

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

async def main():
   async with Client(url=url) as client:
        node_power = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.Power")
        node_power_on = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.PowerOn")
        node_mov_abs = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveAbsolute")
        node_pos = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Position")
        node_ac = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Acceleration")
        node_dac = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Deceleration")
        node_vel = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Velocity")
        
        try:
            if(not await node_power_on.read_value()):
                st.warning("Ligue o motor para iniciar o teste!")
                acesso_mov_abs = False
            elif(await node_vel.read_value() == 0.00 or await node_ac.read_value() == 0.00 or await node_dac.read_value() == 0.00):
                st.warning(":heavy_exclamation_mark: Configure a velocidade!")
                acesso_mov_abs = False
            else:
                acesso_mov_abs = True       

            if motor_on_off:
                st.write("Motor Ligado!")
                await node_power.write_value(dv_True)
                await node_mov_abs.write_value(dv_False)
            else:
                st.write("Motor Desligado!")
                await node_power.write_value(dv_False)
                await node_mov_abs.write_value(dv_False)
            
            value = streamlit_image_coordinates("images/circle_test.png")

            # dimensões da imagem
            altura = 500
            largura = 500

            x = value['x']-(largura/2)
            y = value['y']-(altura/2)
            
            if (x != 0):
                click_coordinate = round((-1)*math.atan(y/x)*180/math.pi,2)

            if (x == 0 and y < 0):
                angle = 90
            elif (x == 0 and y > 0):
                angle = 270
            elif (x > 0 and y == 0):
                angle = 0
            elif (x < 0 and y == 0):
                angle = 180
            elif (x > 0 and y > 0):   
                angle = 360+click_coordinate
            elif (x > 0 and y < 0):   
                angle = click_coordinate
            elif (x < 0 and y > 0):   
                angle = 180+click_coordinate
            elif (x < 0 and y < 0):   
                angle = 180+click_coordinate    
            
            dv = ua.DataValue(ua.Variant(angle, ua.VariantType.Double))  # data value
            await node_pos.write_value(dv)

            if acesso_mov_abs:              # Permite movimento do eixo apenas caso condições sejam alcançadas
                await node_mov_abs.write_value(dv_True) 
            
        except:
    # Prevent the error from propagating into your Streamlit app.
            pass

if __name__ == "__main__":
    asyncio.run(main())