import socket 
import threading


host = '127.0.0.1'
port = 56565

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
nicknames = []

def brodcast(message):
    for client in clients:
        client.send(message)



def handle(client):
    while True:
        try:
            message = client.recv(1024)
            brodcast(message)
        except:
            index = clients.index(client)
            clients.close(client)
            nickname = nicknames[index]
            brodcast(f'{nicknames} has left the chat' .encode(ascii))
            nicknames.remove(nickname)
            break

def recieve():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname for this chat is {nickname}')
        brodcast(f'{nickname} Joined the chat'.encode('ascii'))
        client.send('connected to server' .encode('ascii'))
        thread = threading.Thread(target=handle, args=(client))
        thread.start()


recieve()