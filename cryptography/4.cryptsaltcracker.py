import crypt
from termcolor import colored

def crackpass(cryptword):
	salt = cryptword[0:2]
	dictionary = open("dictionary.txt", 'r')
	for word in dictionary.readlines():
		word = word.strip('\n')
		cryptpass =  crypt.crypt(word, salt)
		if (cryptword == cryptpass):
			print(colored("[+] found password:" + word, 'green'))

def main():
	passFile = open('pass.txt', 'r')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptword = line.split(':')[1].strip('').strip('\n')
			print(colored("[*] Cracking password for: " +user, 'red'))
			crackpass(cryptword)
main()
