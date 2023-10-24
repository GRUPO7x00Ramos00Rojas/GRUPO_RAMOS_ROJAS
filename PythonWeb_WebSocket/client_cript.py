#!/usr/bin/env python
import socket
import uuid
import base64
from cryptography.fernet import Fernet

HEADER = 64
PORT = 2000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.1.104'
ADDR = (SERVER, PORT)

# Genera una clave secreta aleatoria
shared_key = b'pT8ZDjwCvnWkfPEYBm12q2p9srNkM-nWC6Ss9aAcMEw='
cipher_suite = Fernet(shared_key)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    # Cifra el mensaje
    encrypted_msg = cipher_suite.encrypt(msg.encode(FORMAT))
    
    # Envía la longitud del mensaje cifrado
    msg_length = len(encrypted_msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    
    # Envía el mensaje cifrado
    client.send(encrypted_msg)
    
    print(client.recv(2048).decode(FORMAT))

mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])
send(mac_address)

Casos_activos = 123
muertes = 123
msg = "Casos_activos," + str(Casos_activos) + ", muertes," + str(123)
send(msg)

test_data = [12, 12]
data_socket = 'temperature=' + str(test_data[0]) + ',' + 'Humidity=' + str(test_data[1])
send(data_socket)

input()
send("Hello Everyone!")
input()
send("Hello EIE!")

send(DISCONNECT_MESSAGE)
