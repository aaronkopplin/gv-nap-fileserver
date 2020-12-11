import socket
import globals

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((globals.HOST, globals.PORT))
    while True:
        server.listen()
        messenger, address = server.accept()
        print("client connected ", address[0], ":", address[1])
        received_message = messenger.recv(1024)
        if received_message:
            print("> " + received_message.decode("utf-8"))
            messenger.sendall(received_message)
            messenger.close()