#!/usr/local/bin/python
# Netmiko Python Module Library Template

# Importing necessary modules
import paramiko
from getpass import getpass
import time

# Variables for the switch IP or DNS
ip = raw_input("Please enter your IP address: ")
host = ip
username = raw_input("Please enter your username: ")
password = getpass()

# Crreation of a Paramiko SSH client Object
remote_conn_pre = paramiko.SSHClient()

# Disable SSH warnings
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Paramiko SSH connect method
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
print("SSH connection established to " + host)

# Interactive 'shell' using Paramiko invoke_shell() method
remote_conn = remote_conn_pre.invoke_shell()
print("Interactive SSH session established")

# Send commands to switch through interactive 'shell'
remote_conn.send("<cisco command - ex. show version>\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print(output)



# Examples of commands sent to switch through interactive 'shell'
# remote_conn.send("conf t\n")
# time.sleep(.5)
# output = remote_conn.recv(65535)
# print (output)

# remote_conn.send("end\n")
# time.sleep(.5)
# output = remote_conn.recv(65535)
# print (output)