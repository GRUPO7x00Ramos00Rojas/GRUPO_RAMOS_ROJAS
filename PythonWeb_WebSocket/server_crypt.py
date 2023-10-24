#!/usr/bin/env python
import socket
import threading
import base64
from cryptography.fernet import Fernet

HEADER = 64
PORT = 2000
SERVER = '192.168.1.104'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
EXPECTED_STRING = "00:15:5d:3b:2c:f5"

# Clave secreta compartida con el cliente (debe ser la misma que en el cliente)
shared_key = b'pT8ZDjwCvnWkfPEYBm12q2p9srNkM-nWC6Ss9aAcMEw='
#shared_key base64.urlsafe_b64encode(shared_key)
cipher_suite = Fernet(shared_key)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    first_msg_received = False
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            encrypted_msg = conn.recv(msg_length)
            
            # Descifra el mensaje
            msg = cipher_suite.decrypt(encrypted_msg).decode(FORMAT)
            
            if not first_msg_received:
                if msg != EXPECTED_STRING:
                    break
                else:
                    first_msg_received = True
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on address {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
