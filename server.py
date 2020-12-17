import socket
import globals
import xml.etree.ElementTree as ET
import copy
from user import User
import csv


class ConnectedUser():
    def __init__(self, username, speed, port):
        self.username = username
        self.speed = speed
        self.files = []  # list of tuples -> filename, description
        self.port = port

    def addFile(self, fileName, description):
        self.files.append((fileName, description))

    def searchFiles(self, keyword):
        foundFiles = []
        for file in self.files:
            if keyword in file[1]:
                # return the filename associated with that keyword
                foundFiles.append(file[0])  # append filename
        return foundFiles


users = []
# Empty xml that will hold files
files = ET.Element('files')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((globals.HOST, globals.PORT))

    connectedUsers = []
    while True:
        server.listen()
        messenger, address = server.accept()
        peerPort = address[1]
        print("client connected ", address[0], ":", address[1])
        received_message = messenger.recv(1024)
        if received_message:
            lines = received_message.decode("utf-8").split(",")
            connectionType = lines.pop(0)
            if connectionType == globals.INITIAL_CONNECTION:
                username = lines.pop(0)
                connectionSpeed = lines.pop(0)
                newUser = ConnectedUser(username, connectionSpeed, peerPort)
                while lines:
                    fileName = lines.pop(0)
                    fileDescription = lines.pop(0)
                    newUser.addFile(fileName, fileDescription)
                connectedUsers.append(newUser)
                print("added user " + newUser.username + "num users " + str(len(connectedUsers)))
                onlineUsers = [user.username for user in connectedUsers]
                messenger.send(", ".join(onlineUsers).encode())
            elif connectionType == globals.KEYWORD_SEARCH:
                keyword = lines[0]
                fileData = globals.FILE_NOT_FOUND_ERROR
                for user in connectedUsers:
                    print("seraching " + user.username + " for " + keyword)
                    foundFiles = user.searchFiles(keyword)
                    if foundFiles:
                        for filename in foundFiles:
                            fileData += user.speed + "," + user.username + "," + filename + ","

                fileData = fileData[:-1]  # remove the last comma from the string
                fileData = fileData[2:]  # remove the -1 from the befining of the string
                print(fileData)
                messenger.send(fileData.encode())
            elif connectionType == globals.SERVER_NOTIFICATION:
                username = lines.pop(0)
                port = lines.pop(0)
                print(username + " listnening at " + port)
                for user in connectedUsers:
                    if user.username == username:
                        user.port = int(port)
            elif connectionType == globals.FILE_REQUEST:
                username = lines.pop(0)
                print("username = " + username)
                for user in connectedUsers:
                    if user.username == username:
                        print("requested user and port ", username, str(user.port))
                        messenger.send(str(user.port).encode())
            else:
                print("CONNECTION ERROR " + connectionType)

    # while True:
    #     server.listen()
    #     messenger, address = server.accept()
    #     print("client connected ", address[0], ":", address[1])
    #     received_message = messenger.recv(1024)
    #     if received_message:
    #         print("> " + received_message.decode("utf-8"))
    #         message = received_message.decode('utf-8').split()
    #         command = message[0]
    #         username = message[2]
    #         hostname = message[3]
    #         speed = message[4]
    #
    #         if command == 'search':
    #             searchKeyword = message[1]
    #
    #             # Create a copy of the files array
    #             fileMatches = copy.deepcopy(files)
    #             for file in fileMatches:
    #                 foundMatch = False
    #
    #                 # Search for matching keywords
    #                 for keyword in file.find('keywords'):
    #                     if keyword.text == searchKeyword:
    #                         foundMatch = True
    #                         break
    #
    #                 # No matches found - remove it from the list
    #                 if not foundMatch:
    #                     fileMatches.remove(file)
    #
    #             messenger.send(ET.tostring(fileMatches, encoding='utf8', method='xml'))
    #             messenger.close()
    #
    #         elif command == 'get':
    #             fileName = message[1]
    #
    #             #for file in files:
    #                 # Search for file name
    #                 #if file.find('filename').text == fileName:
    #
    #
    #         else:
    #
    #             registered = False
    #             for user in users:
    #                 if username == user.getUsername():
    #                     registered = True
    #             # Parse xml containing file info
    #             try:
    #                 test = messenger.recv(2048).decode()
    #                 root = ET.fromstring(test)
    #
    #                 # Registers new user if the user does not exist already
    #                 if not registered:
    #                     newUser = User(username)
    #                     for file in root.iter('file'):
    #                         files.append(file)
    #                         newUser.addFile(file)
    #                     users.append(newUser)
    #                 else:
    #                     for file in root.iter('file'):
    #                         files.append(file)
    #             except Exception as e:
    #                 print(e)
    #                 pass