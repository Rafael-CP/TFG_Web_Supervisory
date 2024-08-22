# Bibliotecas necessárias para comunicação com servidor OPC UA
import asyncio
from asyncua import *
from opcua import ua

# Bibliotecas necessárias para comunicação com Banco de Dados MySQL
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="opc_ua_tfg"
)

# Endereço do servidor para conexão com o cliente OPC UA
url = "opc.tcp://127.0.0.1:4840/"

# Endereço base OPC UA dos nós utilizados
base_node = "ns=6;s="
param_base_node = "::AsGlobalPV:AxisParam."
control_base_node = "::AsGlobalPV:MpAxisBasic_0."

# Endereço base OPC UA para os nós de alarme
alarm1_base_node = "::AsGlobalPV:Alarm1."
alarm2_base_node = "::AsGlobalPV:Alarm2."
alarm3_base_node = "::AsGlobalPV:Alarm3."

# Endereço das variáveis OPC UA (sucedem o endereço base)
parametros = ['Position',	
  'Distance',	
  'Velocity',	
  'Acceleration',
  'Deceleration',	
  'Direction',	
  'Jog.Velocity',
  'Jog.Acceleration',
  'Jog.Deceleration']

comando = ['Enable',
  'Power',
  'ErrorReset',
  'Home',
  'MoveVelocity',
  'MoveAbsolute',
  'MoveAdditive' ,
  'Stop',
  'JogPositive',
  'JogNegative'
]

analise = [
  'Position',
  'Velocity'
]

status = [ 
  'Error',
  'StatusID',
  'PowerOn',
  'IsHomed',
  'MoveDone',
  'MoveActive'
]

alarms = [
  'Status',
  'Description',
  'Severity',
  'Acknowledgement'
]

# Buffers para armazenamento das variáveis que irão ser inseridas na tabela do banco de dados
buffer_parametros = [0]*len(parametros) 
buffer_comando = [0]*len(comando)
buffer_analise = [0]*len(analise)
buffer_status = [0]*len(status)
buffer_alarms = [0]*len(alarms)

alarm_flag = False
alarm_flag_ack = False

async def main():
  print(f"Conectando ao servidor OPC UA {url} ...") #  Conexão com OPC UA
  mycursor = mydb.cursor()          #  "Cursor" do MySQL (simula uma CLI) 
  alarm_flag = False
  alarm_flag_ack = False
  while True:
    async with Client(url=url) as client: 

      #########################################
      ########## Variáveis de alarme ##########
      alarm_set = await client.get_node(base_node + alarm1_base_node + alarms[0]).read_value()
      alarm_ack = await client.get_node(base_node + alarm1_base_node + alarms[3]).read_value()

      if(not alarm_set):
        alarm_flag = False

      if ((alarm_set and not alarm_flag)):

        for nodes in range(1,len(alarms)): # Leitura dos nós disponíveis no servidor OPC UA
          buffer_alarms[nodes] = await client.get_node(base_node + alarm1_base_node + alarms[nodes]).read_value()  # reads the value within the given node
        
        sql = "INSERT INTO Alarmes VALUE (%s, %s, %s, CURRENT_TIMESTAMP(3))"
        val = buffer_alarms[1:]
        mycursor.execute(sql, val)
        alarm_flag = True
      
      #########################################
      ##### Variáveis para parametrização #####
    
      for nodes in range(len(parametros)): # Leitura dos nós disponíveis no servidor OPC UA
        buffer_parametros[nodes] = await client.get_node(base_node + param_base_node + parametros[nodes]).read_value()  # reads the value within the given node

      sql = "INSERT INTO Parâmetros VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP(3))"
      val = buffer_parametros[:]
      mycursor.execute(sql, val)
 
      #########################################
      ######## Variáveis para comando #########
      for nodes in range(len(comando)): # Leitura dos nós disponíveis no servidor OPC UA
        buffer_comando[nodes] = await client.get_node(base_node + control_base_node + comando[nodes]).read_value()  # reads the value within the given node

      sql = "INSERT INTO Comando VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP(3))" # 3 para mostrar milisegundos
      val = buffer_comando[:]
      mycursor.execute(sql, val)

      #########################################
      ######## Variáveis para análise #########

      for nodes in range(len(analise)): # Leitura dos nós disponíveis no servidor OPC UA
        buffer_analise[nodes] = await client.get_node(base_node + control_base_node + analise[nodes]).read_value()  # reads the value within the given node

      sql = "INSERT INTO Análise VALUES (0, %s, %s, CURRENT_TIMESTAMP(3))"
      val = buffer_analise[:]
      mycursor.execute(sql, val)

      ################################################
      ####### Variáveis para leitura de status #######
      for nodes in range(len(status)): # Leitura dos nós disponíveis no servidor OPC UA
        buffer_status[nodes] = await client.get_node(base_node + control_base_node + status[nodes]).read_value()  # reads the value within the given node
      
      sql = "INSERT INTO Status VALUE (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP(3))"
      val = buffer_status[:]
      mycursor.execute(sql, val)

      ################################################

      mydb.commit() # Atualiza banco de dados

      #await asyncio.sleep(5) # Velocidade em que Banco de dados será atualizado

if __name__ == "__main__":
  asyncio.run(main())