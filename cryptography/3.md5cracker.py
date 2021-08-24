import hashlib
from termcolor import colored

def tryOpen(worldlist):
	global pass_file
	try:
		pass_file = open(wordlist, 'r')
	except:
		print("[!] No such a file at that path")

pass_hash = input("[*] Enter MD5 hash value: ")
wordlist = input("[*] Enter path for wordlist: ")
tryOpen(wordlist)

for word in pass_file:
	print(colored("[-] Trying: " + word.strip("\n"), 'red'))
	enc_wrd = word.encode('utf-8')
	md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	if md5digest == pass_hash:
		print("[+] password found: " + word)
		exit(0)
print("[!] password not in list")
