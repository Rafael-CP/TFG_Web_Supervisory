import streamlit as st  
import asyncio
from asyncua import *
from opcua import ua # MANTENHA O ARQUIVO opcua.py NO DIRETORIO DESTE PROGRAMA - MOTIVO DESCONHECIDO :)
from sqlalchemy import *
import plotly.express as px

st.set_page_config(page_title='Dashboard', page_icon=':peach:', layout='wide')

conn = st.connection('mysql', type='sql') # C:\Users\Rafael\.streamlit\secrets.toml

# Endereço do servidor para conexão com o cliente OPC UA
url = "opc.tcp://127.0.0.1:4840/"

butao1 = st.button(':moyai:',key="1")
butao2 =  st.button(':skull:',key="2")
butao3 = st.button(':eggplant:', key = '3')
placeholder = st.empty()

async def main():
    async with Client(url=url) as client:
            if butao1:
                node = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Velocity")
                dv = ua.DataValue(ua.Variant(10.0, ua.VariantType.Float))  # data value
                await node.write_value(dv)

                node = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveVelocity")
                dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))  # data value
                await node.write_value(dv)
                await asyncio.sleep(0.01) 
                dv = ua.DataValue(ua.Variant(1, ua.VariantType.Boolean))  # data value
                await node.write_value(dv)   

            if butao2:
                node = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Velocity")
                dv = ua.DataValue(ua.Variant(50.0, ua.VariantType.Float))  # data value
                await node.write_value(dv)

                node = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveVelocity")
                dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))  # data value
                await node.write_value(dv)
                await asyncio.sleep(0.01) 
                dv = ua.DataValue(ua.Variant(1, ua.VariantType.Boolean))  # data value
                await node.write_value(dv)      

            if butao3:
                node = client.get_node("ns=6;s=::AsGlobalPV:AxisParam.Velocity")
                dv = ua.DataValue(ua.Variant(100.0, ua.VariantType.Float))  # data value
                await node.write_value(dv)

                node = client.get_node("ns=6;s=::AsGlobalPV:MpAxisBasic_0.MoveVelocity")
                dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))  # data value
                await node.write_value(dv)
                await asyncio.sleep(0.01) 
                dv = ua.DataValue(ua.Variant(1, ua.VariantType.Boolean))  # data value
                await node.write_value(dv)      
                  

            while(True):
                with placeholder.container():
                    df = conn.query('SELECT * FROM análise ORDER BY Time DESC LIMIT 500;', ttl=0)
                
                    #df = conn.query('SELECT * FROM análise;', ttl=0)
                    #print(df)
                    #st.line_chart(data=df, color=None, width=0, height=0, use_container_width=True)

                    col1, col2= st.columns(2)
                    
                    with col1:
                        fig = px.line(df, x=df["Time"], y=df["Position"])
                        fig.update_layout({"uirevision": "foo"}, overwrite=True,width=600)
                        st.write(fig)

                    with col2:
                        fig = px.line(df, x=df["Time"], y=df["Velocity"])
                        fig.update_layout({"uirevision": "foo"}, overwrite=True,width=600)
                        st.write(fig)
            
if __name__ == "__main__":
  asyncio.run(main())