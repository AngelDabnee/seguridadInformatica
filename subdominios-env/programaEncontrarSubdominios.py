'''
    Programa para encontrar los subdominios de un sitio
    Explicar que hace este script
    Desarrollado por Angel Dabnee Gonzalez Rodriguez
'''
import requests
from os import path
import argparse
import sys

parse = argparse.ArgumentParser()
#print(f'{parse}, \n ')
parse.add_argument('-t', '--target', help='Indica el dominio')
parse = parse.parse_args()
'''
    comentario multilinia
    :D !
'''

def main():
    if parse.target:
        if path.exists('subdominios.txt'):
            word_list = open('subdominios.txt', 'r')
            word_list = word_list.read().split('\n')
            
            for subdominio in word_list: 
                url = f'http://{subdominio}.{parse.target}'
                #print(url)
                
                try:
                    requests.get(url, timeout=2.0)
                except requests.ConnectionError:
                    pass
                else:
                    print(f'[+] Subdominio encontrado: {url}')
            for subdominio in word_list: 
                url = f'https://{subdominio}.{parse.target}'
                #print(url)
                
                try:
                    requests.get(url, timeout=2.0)
                except requests.ConnectionError:
                    pass
                else:
                    print(f'[+] Subdominio encontrado: {url}')
        else:
            print('No existe el archivo subdominios.txt')  
    else:
        print('No se ha indicado el dominio')    
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
                