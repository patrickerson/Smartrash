# https://mydevices.com/cayenne/docs_stage/cayenne-mqtt-api/#cayenne-mqtt-api-manually-publishing-subscribing
# Manually Publishing / Subscribing

# Biblioteca para o protocolo MQTT
import paho.mqtt.client as mqtt
import time
import hal

# Variáveis para acesso ao servidor
user = '7c46ccd0-0734-11ea-a38a-d57172a4b4d4'
password = '6cdbad5efa2af6360ed923bf1264bcdaff2b8807'
client_id = '1fdfae50-0737-11ea-a38a-d57172a4b4d4'
server = 'mqtt.mydevices.com'
port = 1883

# Cria o objeto para acessar o servidor (Client ID)
client = mqtt.Client(client_id)

# Informa ao objeto o usuário e senha para acesso ao servidor (MQTT username, MQTT password)
client.username_pw_set(user, password)

# Estabelece a conexão com o servidor (MQTT Server, MQTT Port)
client.connect(server, port)

# MQTT Server, MQTT Port,
client.connect(server, port)

# MQTT Server, MQTT Port,
client.connect(server, port)

movimentos = [False, True, False]

lixo = hal.Lixo(250)
a = 0
while a < 250:

    client.publish('v1/'+user+'/things/'+client_id+'/data/4', lixo.preenchimento_atual(a))
    print(lixo.preenchimento_atual(a)) 
    client.publish('v1/'+user+'/things/'+client_id+'/data/1', lixo.tampa(movimentos[int(a/100)]))
    a += 100
    time.sleep(10)



    