import socket
import os


def Main():
    host = '127.0.0.1'
    port = 50001

    s = socket.socket()
    s.bind((host,port))
    print("server Started")
    s.listen(1)
    while True:
        c, addr = s.accept()
        print("Connection from: " + str(addr))
        filename = ''
        while True:
            data = c.recv(1024).decode('utf-8')
            if not data:
                break
            filename += data
        print("from connected user: " + filename)
        myfile = open(filename, "rb")
        c.send(myfile.read())
        c.close()

if __name__ == '__main__':
    Main()