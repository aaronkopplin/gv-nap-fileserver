import socket
import globals

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((globals.HOST, globals.PORT))
    server.listen()  # listen for connections
    messenger, address = server.accept()  # accept the first connection
    print("client connected ", address[0], ":",address[1])
    while True:
        received_message = messenger.recv(1024)
        received_message = received_message.decode("utf-8")
        if received_message:
            print("> " + received_message)
        else:
            print("client disconnected")
            break