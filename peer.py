import socket
import os
import globals
import xml.etree.ElementTree as ET


class Peer:

    def __init__(self):
        self.files = []
        self.connected = False
        self.serverName = ""
        self.port = -1

    def searchServer(self, searchTerm):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            peer.connect((self.serverName, self.port))
            searchTerm = globals.KEYWORD_SEARCH + "," + searchTerm
            peer.send(searchTerm.encode())
            filename = peer.recv(1024).decode()
            if filename != globals.FILE_NOT_FOUND_ERROR:
                print("success")
            else:
                print("no files found")
            return filename

    def notifyServer(self, username):
        listenForFileRequestsPort = 4000
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            peer.connect((self.serverName, self.port))
            broadcast = globals.SERVER_NOTIFICATION + "," + username + "," + str(listenForFileRequestsPort)
            print("notifying server " + broadcast)
            peer.send(broadcast.encode())
            peer.close()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            peer.bind((globals.HOST, listenForFileRequestsPort))
            print("PEER PORT " + str(peer.getsockname()))
            while True:
                peer.listen()
                messenger, address = peer.accept()
                print("other peer at port" + str(address[1]))
                requestedFileName = messenger.recv(1024).decode()
                with open(requestedFileName, "r") as fileToSend:
                    text = fileToSend.read()
                    messenger.send(text.encode())
                    return requestedFileName

    def fetchFile(self, username, filename):
        portLocation = self.requestHostPort(username)
        if portLocation:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
                print("portLocation " + str(portLocation))
                peer.connect((self.serverName, int(portLocation)))
                peer.send(filename.encode())
                receivedFile = peer.recv(1024).decode()
                print(receivedFile)
                return receivedFile

    def requestHostPort(self, username):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            peer.connect((self.serverName, self.port))
            message = globals.FILE_REQUEST + "," + username
            peer.send(message.encode())
            endPort = peer.recv(1024).decode()
            if endPort:
                return endPort

    def connectToServer(self, servername, port, username, speed):
        self.serverName = servername
        self.port = port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            # peer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # peer.bind((globals.HOST, 4001))
            peer.connect((servername, port))
            with open("publicFiles.csv", "r") as publicFiles:
                fileText = publicFiles.read()
                fileText = globals.INITIAL_CONNECTION + "," + username + "," + speed + "," + fileText
                peer.send(fileText.encode())
                numUsers = peer.recv(1024).decode()
                return numUsers

    def connect(self, command, servername, port, username, hostname, speed, keyword=None):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            try:
                peer.settimeout(5)
                peer.connect((servername, port))

                # Send user info
                peer.send("{} ".format(command).encode())
                peer.send('{} '.format(keyword).encode())
                peer.send('{} '.format(username).encode())
                peer.send('{} '.format(hostname).encode())
                peer.send('{} '.format(speed).encode())

                # Send files if not already connected
                if not self.connected:
                    self.connected = True

                    # Generate xml file that shows files in the current directory
                    self.saveLocalFiles(speed, hostname, username)

                    # Send file info
                    file = open('{}_files.xml'.format(username), 'r')
                    stream = file.read(20498)
                    while stream:
                        peer.send(stream.encode())
                        stream = file.read(2048)
                    file.close()

                # Get list of files from server
                if keyword:
                    test = peer.recv(64000)
                    self.files = ET.fromstring(test)
                peer.close()

            except Exception as e:
                print("Error connecting to server.")

    # Get files from local directory for xml
    def saveLocalFiles(self, speed, hostname, username):
        files = ET.Element('files')
        for filename in os.listdir():
            if os.path.isfile(filename):
                info = ET.SubElement(files, 'file')
                ET.SubElement(info, 'speed').text = speed
                ET.SubElement(info, 'hostname').text = hostname
                ET.SubElement(info, 'filename').text = filename
                keywords = ET.SubElement(info, 'keywords')

                # TODO: Add better keywords
                ET.SubElement(keywords, 'keyword').text = 'test'

                # Random keywords for testing
                import random
                random.seed()
                if random.getrandbits(1):
                    ET.SubElement(keywords, 'keyword').text = 'best'
                if random.getrandbits(1):
                    ET.SubElement(keywords, 'keyword').text = 'worst'

        # Save the files in xml format
        xml = ET.ElementTree(files)
        with open('{}_files.xml'.format(username), 'wb') as fh:
            xml.write(fh, encoding='utf8', method='xml')
