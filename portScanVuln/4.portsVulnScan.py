#!/usr/bin/python3
from socket import*
import argparse
from threading import*

def main():
	parser = argparse.ArgumentParser(prog='advanceScan.py', usage='%(prog)s -d localhost -p 21,22', description='Scan a port on Given Hostname or IP')
	parser.add_argument('-d', '--host', help='Specify Target Domain')
	parser.add_argument('-p', '--port', help='Specify Target ports seprated by comma')

	args = parser.parse_args()
	
	host = args.host
	ports = str(args.port).split(',')
	if(host == None) | (ports[0] == None):
		print(parser.usage)
		exit(0)

main()
