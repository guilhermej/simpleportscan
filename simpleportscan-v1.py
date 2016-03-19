#################################################
# Simple Port Scanner v1.0                      #
# Guilherme Junqueira <contato@solyd.com.br>	#
# https://solyd.com.br/treinamentos				#
#################################################

import socket
import ipaddress
import sys

ipinformado = input("Digite uma rede de IP: ")

ports = range(1, 65535)

try:
    ips = ipaddress.ip_network(ipinformado, strict=False)
except:
    print("IP invalido informado")
    sys.exit()

for ip in ips:
    print("Scanning IP", ip)
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        code = s.connect_ex((str(ip), port))
        s.close()
        if code == 0:
            print("Porta", port, "aberta")
