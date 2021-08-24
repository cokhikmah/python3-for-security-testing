#!/usr/bin/python3
import 	paramiko
import pyfiglet

banner = pyfiglet.figlet_format("SSH LOGIN")

host = input("Enter the IP Address: ")
port = 22
username = "msfadmin"
password = "msfadmin"
command = "cat /etc/passwd"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)
stdin,stdout,sterr =  ssh.exec_command((command))
lines = stdout.readline()
print(lines)
