# this program is the receiver part of Unify.
# its purpose is to receive audio that has
# been transmitted by the sender.py counterpart
# to this program. 


import socket
import pyaudio




# pyAudio streaming constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100




# ------ establish connection with sender ------ #


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





# ------ recieve and emit audio data ------ #


# instantiate pyAudio object
pAud = pyaudio.PyAudio()

# open audio stream
audio_stream = pAud.open(format=FORMAT, 
                        channels=CHANNELS, 
                        rate=RATE,
                        output=True)

#connection loop
while True:
    # receive data from sender module
    received_data = sender_sock.recv(CHUNK)
    
    # break if interrupt in the data
    if not received_data:
        break

    # display the data (emit audio)
    audio_stream.write(received_data)

# close socket and streams when connection broken
sender_sock.close()
audio_stream.stop_stream()
audio_stream.close()
pAud.terminate()
