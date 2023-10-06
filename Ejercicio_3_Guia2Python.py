import serial
import time
import datetime # Importar la librería datetime
import io # Importar la librería file

# Abrir el puerto serial del Arduino
ser = serial.Serial('/dev/ttyACM0', 9600) # Ajustar el nombre y el baudrate según tu configuración

# Crear una lista vacía para almacenar las temperaturas
temperaturas = []

# Leer los valores de temperatura cada segundo
while True:
    # Leer una línea del puerto serial y convertirla a string
    linea = ser.readline().decode('utf-8')
    # Quitar el salto de línea al final
    linea = linea.strip()
    # Intentar convertir la línea a un número flotante
    try:
        temperatura = float(linea)
        # Obtener la hora actual del sistema
        hora = datetime.datetime.now()
        # Formatear la hora como una cadena con el formato HH:MM:SS
        hora_str = hora.strftime("%H:%M:%S")
        # Imprimir la temperatura y la hora en la consola
        print(f"La temperatura es {temperatura} °C a las {hora_str}")
        # Agregar la temperatura a la lista
        temperaturas.append(temperatura)
    except ValueError:
        # Si la línea no es un número, mostrar un mensaje de error
        print(f"Error al leer la temperatura: {linea}")
    except KeyboardInterrupt:
        # Si el usuario presiona Ctrl+C, salir del bucle y calcular el promedio
        print("Programa terminado por el usuario")
        break
    # Esperar 30 segundos antes de leer otro valor
    time.sleep(30)

# Calcular el promedio de las temperaturas
if len(temperaturas) > 0:
    suma = sum(temperaturas)
    cantidad = len(temperaturas)
    promedio = suma / cantidad
    print(f"El promedio de las temperaturas es {promedio} °C")
else:
    print("No se registraron temperaturas")

# Crear un archivo de texto llamado "promedio.txt"
archivo = io.FileIO("promedio.txt", "w")
# Escribir el promedio en el archivo
archivo.write(f"El promedio de las temperaturas es {promedio} °C")
# Cerrar el archivo
archivo.close()
