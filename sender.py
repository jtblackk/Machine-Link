# this program is the sender part of Unify.
# its purpose is to transmit audio from the
# machine running the program to a machine
# running the counterpart program receiver.py


import socket


# create a new socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to this systems ip address + a port
sender_addr = socket.gethostbyname(socket.gethostname())
print("enter a port to use:", end=" ")
sender_port = int(input())
sock.bind((sender_addr, sender_port))

# listen for a connection
sock.listen(4)
print(f"waiting for a connection... connect to {sender_addr} @ port {sender_port}")

# connect to receiver
reciever_socket, receiver_address = sock.accept()
print(f"connection with {receiver_address} established")

# connection loop
while True:
    # get the data to send
    print("enter a message:", end=" ")
    message = input()

    # send the data to the reciever
    reciever_socket.send(bytes(message, "utf-8"))


# close socket when connection loop is broken
sock.close()