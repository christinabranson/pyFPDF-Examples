#!/usr/bin/env python3
import socket, os.path, datetime

def Main():
    host = '127.0.0.1'
    port = 50001

    s = socket.socket()
    s.connect((host, port))

    Filename = input("Type in ur file ")
    s.send(Filename.encode('utf-8'))
    s.shutdown(socket.SHUT_WR)
    data = s.recv(1024).decode('utf-8')
    print(data)
    s.close()

if __name__ == '__main__':
    Main()