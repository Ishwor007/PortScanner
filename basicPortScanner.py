#!/usr/bin/python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = input("[*] Enter the host IP to be scan :")

def portScanner(port):
	if sock.connect_ex((host,port)):
		print(colored("port %d is closed" %(port)), 'red')
	else:
		print(colored("port %d is opened" % (port)), 'green')
for port in range(1,100):
	portScanner(port)
