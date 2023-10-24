import serial

# Configura el puerto serial
puerto_serial = serial.Serial('/dev/ttyACM0', 9600)

try:
    while True:
        # Lee una línea desde el puerto serial y la decodifica a una cadena de caracteres
        linea = puerto_serial.readline().decode('utf-8')
        # Muestra la línea leída en la pantalla
        print(linea)

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C)
    print("Programa interrumpido")

finally:
    # Cierra el puerto serial al finalizar
    puerto_serial.close()
