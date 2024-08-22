import streamlit as st
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

st.title("Documetação")
st.write("Nesta página você poderá consultar a documentação de todos os dispositivos utilizados no projeto.\
         \n A aba inicial fornece o  diagrama de montagem de como os equipamentos estão conectados fisicamente.\
         \n Nas demais abas, é possível fazer o download da documentação!")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Instalações", "Controlador", "Drive", "Servomotor", "Switch"])

with tab1:
    st.image('images/network.png', caption="Diagrama de montagem da bancada de testes",width = 600)

with tab2:
    st.write("O X20CP0483 faz parte da linha Compact-S PLC da B&R, é um controlador compacto, ideal para uma variedade de aplicações de automação industrial, oferecendo uma combinação de desempenho e economia de espaço. As especificações técnicas deste controlador incluem um processador ARM Cortex-A9 de 500 MHz, 256 MB de RAM e possibilidade de comunicação Ethernet, USB, POWERLINK e RS232. Por se tratar de um CLP modular, também permite a capacidade de expansão por meio de módulos adicionais de entrada e saída digitais/analógicos, de fontes externas e até mesmo interfaces de comunicação.")
    
    with open("documentation/CLP/MAX20-en_V4.20.pdf", "rb") as pdf_file:
        PDFfile = pdf_file.read()

        st.download_button(label="Manual CLPs X20",
        data=PDFfile,
        file_name="MAX20-en_V4.20.pdf",key=0)

    with open("documentation/CLP/X20CP04xx_en_V2.22.pdf", "rb") as pdf_file:
        PDFfile = pdf_file.read()

        st.download_button(label="Datasheet CLP x20",
        data=PDFfile,
        file_name="X20CP04xx_en_V2.22.pdf",key=1)

with tab3:
    st.write("A família de produtos ACOPOS, também da B&R, simplifica significativamente o processo de parametrização dos componentes, pois grande parte dos parâmetros dos produtos estão incluídos em bibliotecas do software próprio da B&R, o Automation Studio.")
    st.write("O servo drive modelo ACOPOS 8V1016.00-2 da B&R é uma solução de controle de movimento de alta performance, projetada para atender às exigências de precisão e eficiência em aplicações industriais avançadas Drive. Este servo drive se destaca por sua capacidade de fornecer controle preciso e dinâmico de motores, contribuindo para a otimização dos processos produtivos.")
    st.write("Também oferece opções de personalização através de módulos plug-in. Na bancada didática utilizada, o servo drive vem equipado com três módulos. ")

    with open("documentation/Drive/MAACP2_EN_V2.10.pdf", "rb") as pdf_file:
        PDFfile = pdf_file.read()

        st.download_button(label="Manual Drive ACOPOS",
        data=PDFfile,
        file_name="MAACP2_EN_V2.10.pdf",key=2)

    with open("documentation/Drive/8V1016.00-2_en_V1.7.pdf", "rb") as pdf_file:
        PDFfile = pdf_file.read()

        st.download_button(label="Datasheet Drive ACOPOS",
        data=PDFfile,
        file_name="8V1016.00-2_en_V1.7.pdf",key=3)

with tab4:
    st.write("O motor que será utilizado para testes se trata do modelo 8LS35E2030.D000-0, um servo motor de três fases e quatro polos, fabricado também pela B&R. Possui uma alimentação de 24Vdc e uma potência de 0.66 kW, podendo atingir uma velocidade máxima de 12.000 RPM. Conhecer as características do motor é um fator importante para a configuração e parametrização na plataforma de automação.")
    
    with open("documentation/Servomotor/8LS-A-C-O-P...-3_Users_manual_Motor-V3_Manual-V2.51.pdf", "rb") as pdf_file:
        PDFfile = pdf_file.read()

        st.download_button(label="Manual Servomotor Série 8LS",
        data=PDFfile,
        file_name="8LS-A-C-O-P...-3_Users_manual_Motor-V3_Manual-V2.51.pdf",key=4)

with tab5:
    st.write("Em uma aplicação de controle distribuído, onde diversos computadores precisam se conectar a um Controlador Lógico Programável, o uso de um switch é fundamental para estabelecer uma rede de comunicação eficiente e robusta.")
    st.write("Um switch é um dispositivo de rede que conecta múltiplos dispositivos, como computadores e CLPs, em uma rede local (LAN). Deste modo, o switch irá permitir que vários computadores e dispositivos de controle se conectem ao CLP simultaneamente, estabelecendo uma rede interligada que facilita a comunicação.")
    st.write("O Cisco Catalyst 2960 WS-C2960-24LT-L é um switch que possui 24 portas Ethernet 10/100 Mbps e 2 portas Gigabit Ethernet (10/100/1000) para alta velocidade. A ferramenta de gerenciamento fácil para configuração e monitoramento Cisco Network Assistant também será utilizada para ajustes iniciais. ")

    with open("documentation/Switch/scg_2960.pdf", "rb") as pdf_file:
        PDFfile = pdf_file.read()

        st.download_button(label="Catalyst 2960 Switch Complete Manual",
        data=PDFfile,
        file_name="scg_2960.pdf",key=5)

    with open("documentation/Switch/2960_pbr.pdf", "rb") as pdf_file:
        PDFfile = pdf_file.read()

        st.download_button(label="Guia de primeiros passos do switch Catalyst 2960",
        data=PDFfile,
        file_name="2960_pbr.pdf",key=6)

    with open("documentation/Switch/9368.pdf", "rb") as pdf_file:
        PDFfile = pdf_file.read()

        st.download_button(label="Catalyst 2960 Switch Getting Started Guide",
        data=PDFfile,
        file_name="9368.pdf",key=7)