#!/usr/bin/python3
import socket
from colorama import Fore, Style

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def main():
	ip = input("Enter Target IP")
	for port in range(20,50000):
		banner = retBanner(ip, port)
		if banner:
			print("[+]" + ip + "/" + str(port) + ":" + str(banner))
main()
