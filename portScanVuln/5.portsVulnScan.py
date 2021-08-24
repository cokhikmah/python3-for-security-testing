#!/usr/bin/python3
from socket import*
import argparse
from threading import*
from colorama import Fore, Style

def connScan(host, port):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((host, port))
		print(Fore.WHITE + "[+]{} /tcp Open".format(port))
	except:
		print(Fore.RED + "[-] {} /tcp Closed".format(port))
	finally:
		sock.close()


def portScan(host, ports):
	try:
		tgtIP = gethostbyname(host)
	except:
		print("Unknown Host %s")
	try:
		tgtName = gethostbyaddr(tgtIP)
		print("[+] Scan Results For:  "+ tgtName[0])
	except:
		print("[+] Scan Results For: " + tgtIP)
	setdefaulttimeout(1)
	for port in ports:
		t = Thread(target=connScan, args=(host, int(port)))
		t.start()



def main():
	parser = argparse.ArgumentParser(prog='advanceScan.py', usage='%(prog)s -d example.com or IP -p 21,22', description='Scan a port on Given Hostname or IP')
	parser.add_argument('-d', '--host', help='Specify Target Domain')
	parser.add_argument('-p', '--port', help='Specify Target ports seprated by comma')

	args = parser.parse_args()

	host = args.host
	ports = str(args.port).split(',')
	if(host == None) | (ports[0] == None):
		print(parser.usage)
		exit(0)
	portScan(host,ports)
main()
