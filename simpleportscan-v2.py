#################################################
# Simple Port Scanner v2.0                      #
# Guilherme Junqueira <contato@solyd.com.br>	#
# https://solyd.com.br/treinamentos             #
#################################################

import socket
import ipaddress
import sys
import argparse


# Parser commands
parser = argparse.ArgumentParser(description='Simple TCP port scanning. '
                                             'By Guilherme Junqueira <contato@solyd.com.br>')
parser.add_argument("IP", help="Inform the IPv4 Range (e.g. 200.200.200.0/24)", metavar="IP")
group_top = parser.add_mutually_exclusive_group()
group_top.add_argument("--port", "-p", help="Inform the port", type=int)
group_top.add_argument("--top20", help="Scan for TOP 20 TCP Ports", action="store_true")
group_top.add_argument("--first1023", help="Scan for first 1023 TCP Ports", action="store_true")
group_top.add_argument("--all", help="Scan all 65535 TCP Ports", action="store_true")
parser.add_argument("--timeout", help="Inform the timeout in seconds (Default=0.1)", default=0.1, type=float)
args = parser.parse_args()

# Validate IPv4 Network
try:
    network = ipaddress.ip_network(args.IP, strict=False)
except:
    print("Error: Not a valid IP network\n")
    parser.print_usage()
    sys.exit()

# Validate TCP Port
if args.port and (args.port < 1 or args.port > 65535):
    print("Error: Port out of range, especify a value between 1 and 65535\n")
    parser.print_usage()
    sys.exit()

if args.top20:
    ports = [21, 22, 25, 53, 80, 110, 135, 137, 138, 139, 143, 443, 465, 587, 995, 1521, 2525, 3306, 8000, 8080]
elif args.first1023:
    ports = range(1, 1023)
elif args.all:
    ports = range(1, 65535)
else:
    ports = [args.port]

timeout = args.timeout


def Scanner(ips, ports):
    for ip in ips:
        hosts=[]
        print("Scanning: " + str(ip))
        for port in ports:
            sys.stdout.write("Port: " + str(port))
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(timeout)
                code = s.connect_ex((str(ip), port))
                s.close()
                if code == 0:
                    print(" -> Open")
                    hosts.append(ip)
                else:
                    sys.stdout.write("\r")
                    sys.stdout.flush()
            except:
                pass
        if len(hosts) == 0:
            print("Nenhum porta aberta encontrada")


Scanner(network, ports)






