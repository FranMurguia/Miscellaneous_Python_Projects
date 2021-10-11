# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:48:15 2021

@author: FranJa
"""
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and Port to make the connection
my_socket.connect(("data.pr4e.org", 80))

cmd = "GET http://http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
my_socket.send(cmd)

# HTTP Header

# HTTP Body

while True:
    data = my_socket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

my_socket.close()


