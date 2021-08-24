#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("IP Address: ")
port = int(input("Port: "))

def portScan(port):
	result = sock.connect_ex((host, port))
	if result == 0:
		print("PORT IS OPEN")
	else:
		print("PORT IS ClOSED")

portScan(port)
