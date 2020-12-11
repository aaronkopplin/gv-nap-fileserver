import socket
import globals


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer:
        try:
            peer.connect((globals.HOST, globals.PORT))
            message = input("> ")
            if message == "exit": break
            peer.sendall(message.encode())
        except:
            choice = input("the host is not online. Try again? (y/n)\n")
            if choice == "y":
                continue
            elif choice == "n":
                break
            else:
                print("error: unreadable input.")
                break

