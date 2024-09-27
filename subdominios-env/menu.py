import os
from bannergraby import banner


print("Sistema para pruebas de seguridad informática")
print("Versión 1.0")
print("Desarrollado por: Angel Dabnee")

x = True
opcion = 0

os.system("cls")

while x:
    print("\nOpción 1: Encontrar IP de una URL.")
    print("Opción 2: Encontrar IP opcion 2.")
    print("Opción 3: Encontrar subdominios.")
    print("Opción 4: Banner Grabbing.")
    print("Opción 5: Wad.")
    print("Opción 6: Escaneo de Puertos.")
    print("Opción 7: Salir.")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1: 
            vistima = input("Ingrese el dominio: ")
            print("Encontrar IP de una URL")
            os.system("py getip.py -t " + vistima)
            input("Presione Enter para continuar...")
            os.system("cls")
        elif opcion == 2:
            vistima = input("Ingrese el dominio: ")
            print("Encontrar IP de una URL")
            os.system("py getip2.py -t " + vistima)
            input("Presione Enter para continuar...")
            os.system("cls")
        #Encontrar una URL 
        elif opcion == 3:
            vistima = input("Ingrese el dominio: ")
            print("Encontrar subdominios")
            os.system("py programaEncontrarSubdominios.py -t " + vistima)
            input("Presione Enter para continuar...")
            os.system("cls")
        #Banner
        elif opcion == 4:
            vistima = input("Ingrese el dominio o IP: ")
            puerto_input = input("Ingrese el puerto (default 21): ")
            puerto = int(puerto_input) if puerto_input else 21
            
            print("Banner Grabbing")
            banner_info = banner(vistima, puerto)
            print(f"Banner recibido:\n{banner_info}")
            
            input("Presione Enter para continuar...")
            os.system("cls") 

        elif opcion == 5:
            print("Wad")
        elif opcion == 6:
            print("Escaneo de Puertos")
        elif opcion == 7:
            print("Saliendo del sistema...")
            x = False
        else:
            print("Opción no válida, intenta de nuevo.")
    
    except ValueError:
        print("Error: Ingrese un número válido.")
