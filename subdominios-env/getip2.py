import socket
import sys
import argparse
import os

# Definición del parser de argumentos
parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Indica la URL sin HTTP')

# Analiza los argumentos proporcionados
parse = parse.parse_args()

# Función para obtener la IP de una URL con nslookup
def getIP(url):
    try:
        # Crear el comando nslookup
        command = f"nslookup {url}"
        
        # Ejecutar el comando y capturar la respuesta
        respuesta = os.system(command)
        
        # Verificamos el código de salida del comando
        if respuesta == 0:
            print(f"Consulta nslookup para {url} realizada con éxito.")
        else:
            print(f"Error al ejecutar nslookup para {url}.")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    if parse.target:
        try:
            getIP(parse.target)
        except Exception as e:
            print(f"No se pudo resolver la URL: {e}")
    else:
        print("Ingrese una dirección sin HTTP.")

# Punto de entrada del programa
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por teclado detectada. Saliendo del programa...")
        sys.exit()





'''command = "nslookup google.com"
respuesta = os.system(command)

print(respuesta)'''