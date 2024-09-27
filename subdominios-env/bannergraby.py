import socket
import sys
import argparse


parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Indica el dominio')
parse = parse.parse_args()


def banner (ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        print(str(s.recv(1024)))
        banner = s.recv(1024)
        return banner
    except:
        return  
    
def main():
    if parse.target:
        try:
            ip = parse.target
            #ip = socket.gethostbyname(parse.target)
            port = 21
            banner(ip, port)
    
        except:
            print('y la ip?')
            
            
            
            
'''
import socket
import argparse
import sys

def banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).decode('utf-8')
        s.close()
        return banner
    except socket.error as err:
        return f"Error en la conexión: {err}"

def main():
    parser = argparse.ArgumentParser(description='Banner grabbing tool')
    parser.add_argument('-t', '--target', required=True, help='Indica el dominio o IP')
    parser.add_argument('-p', '--port', type=int, default=21, help='Puerto a escanear (default 21)')
    args = parser.parse_args()

    ip = args.target
    port = args.port

    print(f"Escaneando {ip}:{port}")
    banner_info = banner(ip, port)

    if banner_info:
        print(f"Banner recibido:\n{banner_info}")
    else:
        print("No se recibió ningún banner.")

if __name__ == "__main__":
    main()
'''''