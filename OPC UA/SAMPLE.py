# Bibliotecas necessárias para comunicação com servidor OPC UA
import asyncio
from asyncua import *
from opcua import ua

# Endereço do servidor para conexão com o cliente OPC UA
url = "opc.tcp://127.0.0.1:4840/"

# Endereço base OPC UA dos nós utilizados
base_node = "ns=6;s="
param_base_node = "::AsGlobalPV:AxisParam."
control_base_node = "::AsGlobalPV:MpAxisBasic_0."

analise = [
  'Position',
  'Velocity'
]
buffer_analise = [0]*len(analise)

async def main():
    print(f"Conectando ao servidor OPC UA {url} ...") #  Conexão com OPC UA

    for nodes in range(len(analise)): # Leitura dos nós disponíveis no servidor OPC UA
            buffer_analise[nodes] = await client.get_node(base_node + control_base_node + analise[nodes]).read_value() 

    val = buffer_analise[:]
    #await node_power_on.read_value()
    #print


if __name__ == "__main__":
  asyncio.run(main())  