# this program is the receiver part of Unify.
# its purpose is to receive audio that has
# been transmitted by the sender.py counterpart
# to this program. 


import socket


# create a new socket
sender_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the sender address and port
print("enter the sender's IP address:", end=" ")
sender_addr = input()
print("enter the sender's port:", end=" ")
sender_port = int(input())

# connect to the sender
sender_sock.connect((sender_addr, sender_port))
print("connected to sender")


while True:
    recieved_data = sender_sock.recv(1024)
    decoded_data = recieved_data.decode('utf-8')

    print("sender:", decoded_data)
    if decoded_data == "!quit":
        break


    