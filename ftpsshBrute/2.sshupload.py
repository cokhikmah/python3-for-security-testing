#!/usr/bin/python3
import 	paramiko
import pyfiglet

banner = pyfiglet.figlet_format("SSH File Upload")

host = input("Enter the IP Address: ")
port = 22
username = input("Enter Username For SSH: ")
password = input("Enter Password For SSH: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)
sftp = ssh.open_sftp()

server_path = input("Enter the file name with path (/tmp/test.txt): ")
localpath = input("Enter File name to upload (sam.txt): ")
sftp.put(localpath, server_path)

sftp.close()
ssh.close()
