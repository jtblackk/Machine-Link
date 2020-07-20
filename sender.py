# this program is the sender part of Unify.
# its purpose is to transmit audio from the
# machine running the program to a machine
# running the counterpart program receiver.py


import socket
import pyaudio





# pyAudio streaming constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 44100





# ------ choose audio device to stream ------- #


# instantiate pyAudio object
pAud = pyaudio.PyAudio()

# list audio devices
print("Available audio devices:")
for device_index in range(0, pAud.get_device_count()):
    device_info = pAud.get_device_info_by_index(device_index)
    device_name = device_info.get("name")
    if str(device_name).count("Virtual") or str(device_name).count("Mic") or str(device_name).count("Stereo"):
        print(f"\t{device_index}: {device_name}")

# choose audio device
print("Enter the number id of the device to stream from")
chosen_device = int(input())
audio_device = pAud.get_device_info_by_index(chosen_device)





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
receiver_sock, receiver_addr = sock.accept()
print(f"connection with {receiver_addr} established")




# ------ send audio data ------ #


# send header (number of channels)
receiver_sock.send(bytes(str(audio_device.get('maxInputChannels')), "utf-8"))

# open audio stream
audio_stream = pAud.open(format=FORMAT, 
                        channels=audio_device.get('maxInputChannels'), 
                        rate=RATE, 
                        input=True, 
                        frames_per_buffer=CHUNK,
                        input_device_index=audio_device.get('index'))

# connection loop
while True:
    try:
        # get the data to send
        data = audio_stream.read(CHUNK)

        # send the data to the reciever
        receiver_sock.send(data)
    except:
        pass

# close socket and streams when loop is broken
sock.close()
audio_stream.stop_stream()
audio_stream.close()
pAud.terminate()

