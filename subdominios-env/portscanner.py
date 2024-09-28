"""import sys
import socket
import argparse
import os 
from os import path

parse = argparse.ArgumentParser(description="Escanear puertos en un dominio o IP.")
parse.add_argument('-t', '--target', help='Indica el dominio o IP', required=True)
args = parse.parse_args()

def main():
    if path.exists('puertos.txt'):
        with open('puertos.txt', 'r') as wordList:
            puertos = wordList.read().splitlines()
        
        if not puertos:
            print('No se encontraron puertos')
            return
        
        #target = args.target
        
        
        for puerto in puertos:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            respuesta = s.connect_ex((args.target, int(puerto)))    
            if respuesta == 0:
                print(f'Puerto {puerto} abierto')
            else:
                print(f'Puerto {puerto} cerrado')
            
            s.close()
            
            
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
"""
# portscanner.py
import socket
import os
from os import path

def scan_ports(target):
    if path.exists('puertos.txt'):
        with open('puertos.txt', 'r') as wordList:
            puertos = wordList.read().splitlines()
        
        if not puertos:
            print('No se encontraron puertos')
            return
        
        for puerto in puertos:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            respuesta = s.connect_ex((target, int(puerto)))
            if respuesta == 0:
                print(f'Puerto {puerto} abierto')
            else:
                print(f'Puerto {puerto} cerrado')
            
            s.close()
    else:
        print("El archivo puertos.txt no existe.")
