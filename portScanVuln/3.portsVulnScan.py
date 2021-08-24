#!/usr/bin/python3
from socket import*
import pyfiglet
import sys

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)
if len(sys.argv) == 2:
	targetIP = gethostbyname(sys.argv[1])
else:
	print("Invalid argument")
try:
	for i in range(20,1025):
		s = socket(AF_INET, SOCK_STREAM)
		result = s.connect_ex((targetIP,i))
		if (result == 0):
			print('Port {}: Open'.format(i))
			s.close()
except KeyboardInterupt:
	print("\n Exitting Program")
	sys.exit()
except socket.gaierror:
	print("\n Hostname could not be Resolved")
	sys.exit()
except socket.error:
	print("\n Server not responding")
	sys.exit()
