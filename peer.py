import socket
import globals


class Peer:

    def connect(self, servername, port, username, hostname, speed):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
            try:
                peer.connect((servername, port))
                peer.send(username.encode())
                peer.send(hostname.encode())
                peer.send(speed.encode())
            except:
                print("Error connecting to server.")

