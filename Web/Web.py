import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development


st.set_page_config(page_title='Dashboard', page_icon=':peach:', layout='wide')

conn = st.connection('mysql', type='sql') # C:\Users\Rafael\.streamlit\secrets.toml

butao = st.button(':sunglasses:',key="1")
if butao:
    print('teste')

# creating a single-element container
placeholder = st.empty()

# near real-time / live feed simulation
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
        
        #st.markdown("### Detailed Data View")
        #st.dataframe(df)

        #time.sleep(0.05)
        #st.write('')