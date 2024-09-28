# seguridadInformatica
# Network Tools Project

Este repositorio contiene una colección de herramientas de red escritas en Python. Cada herramienta cumple con una función específica como banner grabbing, escaneo de puertos, obtención de IPs y descubrimiento de subdominios.

## Archivos incluidos

### 1. **bannegraby.py**
Herramienta para realizar **banner grabbing**. Se conecta a un puerto específico de una IP o dominio y recupera el banner de respuesta.

#### Uso:
```bash
python bannegraby.py <IP> <PORT>
python bannegraby.py 192.168.1.1 80
python getip.py <domain>
python getip2.py example.com
python menu.py
python portscanner.py <IP/Domain> <file_with_ports>
python portscanner.py 192.168.1.1 ports.txt
python subdomain_finder.py <domain> <subdomains_list>
python subdomain_finder.py example.com subdomains.txt
Requisitos

    Python 3.x
    Bibliotecas adicionales:
        socket (incluida en la biblioteca estándar de Python)

Instalación

    Clona este repositorio:

git clone https://github.com/tu_usuario/network-tools.git

Puedes copiar y pegar este contenido en tu archivo `README.md` para que aparezca en tu repositorio.
NOTA: EN LA RAMA DEV ENCONTRARÁ MAYOR INFORMACIÓN NO TERMINADA PERO FUNCIONAL
