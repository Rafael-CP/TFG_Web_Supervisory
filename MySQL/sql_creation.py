import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="opc_ua_tfg" # 'USE opc_ua_tfg' in the CLI
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE OPC_UA_TFG") # if database is not yet created

# Creating the tables for the desired variables
mycursor.execute("CREATE TABLE Parâmetros (Position FLOAT, Distance FLOAT, Velocity FLOAT, Acceleration FLOAT, Deceleration FLOAT, Direction TINYINT, JogVelocity FLOAT, JogAcceleration FLOAT, JogDeceleration FLOAT, Time TIMESTAMP(3))")
mycursor.execute("CREATE TABLE Comando (Enable BOOL, Power BOOL, ErrorReset BOOL, Home BOOL, MoveVelocity BOOL, MoveAbsolute BOOL, MoveAdditive BOOL, Stop BOOL, JogPositive BOOL, JogNegative BOOL, Time TIMESTAMP(3))")
mycursor.execute("CREATE TABLE Análise (id INT AUTO_INCREMENT PRIMARY KEY, Position FLOAT(3), Velocity Float(3), Time DATETIME(3))")
mycursor.execute("CREATE TABLE Status (Error BOOL, StatusID INT, PowerOn BOOL, IsHomed BOOL, MoveDone BOOL, MoveActive BOOL, Time TIMESTAMP(3))")
mycursor.execute("CREATE TABLE Alarmes (Descrição VARCHAR(100), Severidade INT, Reconhecimento BOOL, Time TIMESTAMP(3))")




#mycursor.execute("DROP TABLE Parâmetros, Comando, Análise, Status, Alarmes") # in case it needs to drop all the tables
