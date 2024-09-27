import socket
import sys
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Indica la URL sin HTTP')

parse = parse.parse_args()

def getIP(url):
    try:
        ip = socket.gethostbyname(url)
        print(f"La IP de {url} es: {ip}")
    except:
        return "No se pudo resolver la URL" 

def main():
    if parse.target:
        try:
            getIP(parse.target)
            
        except:
            print("No se pudo resolver la URL")
    else:
        print("Ingrese una dirección sin HTTP ")
        
        
if __name__ == '__main__': #o en lugar de eso es __main__
    try: 
        main()
    except KeyboardInterrupt:
        sys.exit()