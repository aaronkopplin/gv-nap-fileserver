import socket
import globals

#
# class Peer:
#     def __init__(self):

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
    peer.connect((globals.HOST, globals.PORT))
    while True:
        message = input("> ")
        peer.sendall(message.encode())
