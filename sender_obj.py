# this program is the sender part of Unify.
# its purpose is to transmit audio from the
# machine running the program to a machine
# running the counterpart program receiver.py


import socket
import pyaudio
import random as r


class sender:
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    p = pyaudio.PyAudio()
    receiver_socket = None


    # returns a list of the audio devices available for use
    # removes duplicate items and filters out invalid options
    def get_audio_devices(self):
        audio_device_list = []
        for index in range(0, self.p.get_device_count()):
            device = self.p.get_device_info_by_index(index)
            if device.get('maxInputChannels'):
                if not (str(device.get('name')).count('(') and not str(device.get('name')).count(')')):
                    audio_device_list.append(device.get('name'))
        return frozenset(audio_device_list)

    # connect to the receiver
    def create_socket(self):
        # create a new socket
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket
        self.sender_address = socket.gethostbyname(socket.gethostname())
        self.sender_port = r.randint(6000,8000)
        self.sender_socket.bind((self.sender_address, self.sender_port))

    def connect_to_receiver(self):
        # listen for a connection
        self.sender_socket.listen(4)

        # connect to the receiver
        self.receiver_socket, self.receiver_address = self.sender_socket.accept()

    # send a header and the audio data stream to the receiver
    def stream_audio(self, device_name):
        # find the index of the device provided
        device_index = int()
        for index in range(0, self.p.get_device_count()):
            if self.p.get_device_info_by_index(index).get('name') == device_name:
                device_index = index

        # send header
        device_info = self.p.get_device_info_by_index(device_index)
        self.receiver_socket.send(bytes(str(device_info.get('maxInputChannels')), "utf-8"))

        # open audio stream
        self.audio_stream = self.p.open(format = self.FORMAT,
                                        channels = device_info.get('maxInputChannels'),
                                        rate = self.RATE,
                                        input = True,
                                        frames_per_buffer = self.CHUNK_SIZE,
                                        input_device_index=device_info.get('index'))

        # connection loop
        while True:
            try:
                # get the data to send
                data = self.audio_stream.read(self.CHUNK_SIZE)

                # send the data to the receiver
                self.receiver_socket.send(data)
            except: # break if there's an interruption in the data flow
                break
