#!/usr/bin/python3
import 	paramiko
import pyfiglet

banner = pyfiflet.figlet_format("SSH file download")

host = input("Enter the IP Address: ")
port = 22
username = "msfadmin"
password = "msfadmin"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)
sftp = ssh.open_sftp()

server_path = input("Enter the file name (/home/msfadmin/readme.txt): ")
localpath = input("Enter output file name (readme.txt): ")
sftp.get(server_path,localpath)
