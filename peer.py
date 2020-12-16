import socket
import os
import globals
import xml.etree.ElementTree as ET


class Peer:

    def __init__(self):
        self.files = []

    def connect(self, command, servername, port, username, hostname, speed, keyword=None):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            try:
                peer.connect((servername, port))

                # Send user info
                peer.send("{} ".format(command).encode())
                if keyword:
                    peer.send('{} '.format(keyword).encode())
                peer.send(username.encode())
                peer.send(hostname.encode())
                peer.send(speed.encode())

                # Send file info
                file = open('filelist.xml', 'r')
                stream = file.read(1024)
                while stream:
                    peer.send(stream.encode())
                    stream = file.read(1024)
                file.close()

                # Get list of files from server
                self.files = ET.fromstring(peer.recv(64000))

            except Exception as e:
                print(e)
                print("Error connecting to server.")
