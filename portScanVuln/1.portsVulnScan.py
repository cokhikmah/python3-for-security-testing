#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.42.111"
port = 53

def portScan(port):
	result = sock.connect_ex((host, port))
	if result == 0:
		print("PORT IS OPEN")
	else:
		print("PORT IS ClOSED")

portScan(port)
