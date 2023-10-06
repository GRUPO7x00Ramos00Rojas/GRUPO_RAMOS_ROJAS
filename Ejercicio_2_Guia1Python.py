import smbus
import time

address = 0x08 # Dirección del dispositivo

bus = smbus.SMBus(1) # Interfaz I2C a utilizar

while True:
    numero = bus.read_byte(address) # Lee el número enviado por Arduino
    print(f"Número recibido: {numero}")
    time.sleep(0.2) #Realiza la solicitud de datos cada 0.2s
