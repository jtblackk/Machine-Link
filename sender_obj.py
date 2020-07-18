
import socket
import pyaudio
import random as r

class sender:
    # properties
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    # socket


    # methods
    def __init__(self):
        # instantiate pyAudio object
        self.p = pyaudio.PyAudio()

    def create_sender_socket(self):
        # create a new socket
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket
        self.sender_address = socket.gethostbyname(socket.gethostname())
        self.sender_port = r.randint(6000,8000)
        self.sender_socket.bind((self.sender_address, self.sender_port))

    def establish_connection(self):
        # listen for a connection
        self.sender_socket.listen(4)
        print(f"waiting for a connection... connect to {self.sender_address} @ {self.sender_port}")

        # connect to the receiver
        self.receiver_socket, self.receiver_address = self.sender_socket.accept()
        print(f"connection with {self.receiver_address} established")


    def stream_audio(self, device_index):
        # send header
        device_info = self.p.get_device_info_by_index(device_index)
        self.receiver_socket.send(bytes(str(device_info.get('maxInputChannels')), "utf-8"))

        # open audio stream
        self.audio_stream = self.p.open(format = self.FORMAT,
                                        channels = device_info.get('maxInputChannels'),
                                        rate = self.RATE,
                                        input = True,
                                        frames_per_buffer = self.CHUNK,
                                        input_device_index=device_info.get('index'))

        # connection loop
        while True:
            # get the data to send
            data = self.audio_stream.read(self.CHUNK)

            # send the data to the receiver
            self.receiver_socket.send(data)

        # close socket and streams
        self.sender_socket.close()
        self.audio_stream.stop_stream()
        self.audio_stream.close()
        self.p.terminate()
