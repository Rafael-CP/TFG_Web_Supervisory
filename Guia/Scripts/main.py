# Bibliotecas necessárias para comunicação com servidor OPC UA
import asyncio
import asyncua as ua
from asyncua import *
import streamlit as st

# Endereço do servidor para conexão com o cliente OPC UA
url = "opc.tcp://127.0.0.1:4840/"

# Endereços base OPC UA dos nós utilizados
# Nó base - todas as variáveis vão possuir este prefixo
base_node = "ns=6;s="                  
# Nó de controle - variáveis do programa Program 
# do tipo MpAxisBasic de nome AxisBasic
control_node = "::Program:AxisBasic." 
# Nó de parametrização - variáveis do programa Program 
# do tipo MpAxisBasicParType de nome AxisParam
param_node = "::Program:AxisParam." 

# Variável de potência do motor AxisBasic.Power
cPower = base_node + control_node + "Power" 
# Variável de acionamento do movimento AxisBasic.MoveVelocity
cMoveVelocity = base_node + control_node + "MoveVelocity" 

# Variável de velocidade AxisBasic.Velocity (para monitoramento - leitura)
cVelocity = base_node + control_node + "Velocity" 

# Variável de velocidade AxisParam.Velocity para escrita
pVelocity = base_node + param_node + "Velocity" 

async def main():
    print(f"Conectando ao servidor OPC UA {url}")
    print("===================================================================")
    async with Client(url=url) as client:

        # Para se ter acesso ao nó, utilize os seguintes comandos: 
        cPower_node = client.get_node(cPower)
        cMoveVelocity_node = client.get_node(cMoveVelocity)
        cVelocity_node = client.get_node(cVelocity)
        pVelocity_node = client.get_node(pVelocity)
        # Isso irá criar um objeto do tipo node da variável desejada
        # no qual podemos utilizar metodos de leitura e escrita

        # Para ler uma variável, basta usar o método read_value() no objeto node criado. Exemplo:
        print("Estado do motor: " + str(await cPower_node.read_value()))   # True = ON | False = OFF
        print("Velocidade do eixo: " + str(await cVelocity_node.read_value()))    
        print("===================================================================")
        ''' Para a escrita devemos primeiro transformar a variável 
        num objeto compativel com o padrão OPC UA, e para isso
        seguimos a seguinte estrutura:
        ua.DataValue(ua.Variant([VALOR], ua.VariantType.[TIPO])) 
        Atente-se bastante ao tipo que for colocado para evitar erros'''

        # Criando variáveis booleanas que podem ser usadas ao longo do programa:
        dv_True = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean)) 
        dv_False = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean)) 

        # Variável do tipo float, para alterar a velocidade na parametrização do motor
        dvVelocity = ua.DataValue(ua.Variant(10.0, ua.VariantType.Float)) 
        
        # Para escrever na variável, basta utilizar o método write_value,
        # tendo como argumento o valor com tipo correto 
        await pVelocity_node.write_value(dvVelocity)    # Mudando valor da velocidade
        await cPower_node.write_value(dv_True)          # Ligando motor
        
        print("Ligando motor...")
        print("===================================================================")
        # Ao executar comandos de potência, use um temporizador entre eles para evitar erros
        await asyncio.sleep(0.5)                        # Aguarda 0.5 segundo para proxima escrita
        await cMoveVelocity_node.write_value(dv_True)   # Acionando controle de velocidade

        await asyncio.sleep(0.5)  
        print("Estado do motor: " + str(await cPower_node.read_value()))   # True = ON | False = OFF
        print("Velocidade do eixo: " + str(await cVelocity_node.read_value()))    
        print("===================================================================")

        print("Motor em movimento por 5s (Confira no seu software de automação!)")
        print("===================================================================")
        await asyncio.sleep(5) 

        await cMoveVelocity_node.write_value(dv_False)   # Desligando controle de velocidade
        print("Desligando motor...")
        print("===================================================================")
        await asyncio.sleep(0.5)  
        await cPower_node.write_value(dv_False)          # Desligando motor    
        
        await asyncio.sleep(0.5)  
        print("Estado do motor: " + str(await cPower_node.read_value()))   # True = ON | False = OFF
        print("Velocidade do eixo: " + str(await cVelocity_node.read_value()))    
        print("===================================================================")
        
if __name__ == "__main__":
  asyncio.run(main())