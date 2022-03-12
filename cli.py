import socket 
import threading


host = '127.0.0.1'
port = 56564


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

def sendmessage():
    while 1:
        input1 = input()
        input1 = """ + input1 + """
        client.sendall(input1.encode('ascii'))

def getmessage():
    while 1:
        message = client.recv(1024).decode('ascii')
        print(message)

while 1:
    thread = threading.Thread(target=sendmessage)
    thread.start()
    thread2 = threading.Thread(target=getmessage)
    thread2.start()