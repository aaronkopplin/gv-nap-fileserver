import socket
import globals
import xml.etree.ElementTree as ET
import copy

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
                searchKeyword = message[1]

                # Create a copy of the files array
                fileMatches = copy.deepcopy(files)
                for file in fileMatches:
                    foundMatch = False

                    # Search for matching keywords
                    for keyword in file.find('keywords'):
                        if keyword.text == searchKeyword:
                            foundMatch = True
                            break

                    # No matches found - remove it from the list
                    if not foundMatch:
                        fileMatches.remove(file)

                messenger.send(ET.tostring(fileMatches, encoding='utf8', method='xml'))
                messenger.close()
            else:

                # Parse xml containing file info
                try:
                    test = messenger.recv(2048).decode()
                    root = ET.fromstring(test)
                    for file in root.iter('file'):
                        files.append(file)
                except Exception as e:
                    print(e)
                    pass