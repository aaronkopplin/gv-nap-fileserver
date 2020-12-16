import socket
import globals
import xml.etree.ElementTree as ET

users = []

# Empty xml that will hold files
files = ET.Element('files')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((globals.HOST, globals.PORT))

    while True:
        server.listen()
        messenger, address = server.accept()
        print("client connected ", address[0], ":", address[1])
        received_message = messenger.recv(1024)
        if received_message:
            print("> " + received_message.decode("utf-8"))
            message = received_message.decode('utf-8').split()
            command = message[0]
            if command == 'search':
                keyword = message[1]

            # Parse xml containing file info
            root = ET.fromstring(messenger.recv(1024).decode())
            for file in root.iter('file'):
                files.append(file)
            messenger.send(ET.tostring(files, encoding='utf8', method='xml'))
            messenger.close()
