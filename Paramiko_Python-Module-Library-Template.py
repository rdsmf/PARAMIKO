#!/usr/local/bin/python
# Paramiko Python Module Library Template

# Importing necessary modules
import paramiko
import time

# Variables for the switch IP or DNS
ip = "<ip address / dns>"
host = ip
username = "<username>"
password = "<password>"

# Crreation of a Paramiko SSH client Object
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre

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
