import socket
import os
import globals
import xml.etree.ElementTree as ET


class Peer:

    def __init__(self):
        self.files = []
        self.connected = False

    def connect(self, command, servername, port, username, hostname, speed, keyword=None):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            try:
                peer.settimeout(5)
                peer.connect((servername, port))

                # Send user info
                peer.send("{} ".format(command).encode())
                peer.send('{} '.format(keyword).encode())
                peer.send(username.encode())
                peer.send(hostname.encode())
                peer.send(speed.encode())

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
