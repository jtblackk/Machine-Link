# this program is the sender part of Unify.
# its purpose is to transmit audio from the
# machine running the program to a machine
# running the counterpart program receiver.py


import socket
import pyaudio




# pyAudio streaming constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100




# ------ establish connection with reciever ------ #


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
reciever_sock, receiver_addr = sock.accept()
print(f"connection with {receiver_addr} established")





# ------ send audio data ------ #


# instantiate pyAudio object
pAud = pyaudio.PyAudio()

# get default audio input device
audio_device = pAud.get_default_input_device_info()

# open audio stream
audio_stream = pAud.open(format=FORMAT, 
                        channels=CHANNELS, 
                        rate=RATE, 
                        input=True, 
                        frames_per_buffer=CHUNK,
                        input_device_index=audio_device.get('index'))

# connection loop
while True:
    # get the data to send
    data = audio_stream.read(CHUNK)

    # send the data to the reciever
    reciever_sock.send(data)

# close socket and streams when loop is broken
sock.close()
audio_stream.stop_stream()
audio_stream.close()
pAud.terminate()

