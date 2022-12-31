import socket
import pyaudio
import random as r


class sender:
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    p = pyaudio.PyAudio()

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

    # create a socket for sending data
    def create_socket(self):
        # create a new socket
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # bind the socket
        self.sender_address = socket.gethostbyname(socket.gethostname())
        self.sender_port = r.randint(6000, 8000)
        self.sender_socket.bind((self.sender_address, self.sender_port))

    # send a header and the audio data stream to the receiver
    def stream_audio(self, receiver_address, receiver_port, device_name):
        # find the index of the device provided
        device_index = int()
        for index in range(0, self.p.get_device_count()):
            if self.p.get_device_info_by_index(index).get('name') == device_name:
                device_index = index

        # send header
        device_info = self.p.get_device_info_by_index(device_index)
        self.sender_socket.sendto(bytes(str(device_info.get(
            'maxInputChannels')), "utf-8"), (receiver_address, receiver_port))

        # open audio stream
        self.audio_stream = self.p.open(format=self.FORMAT,
                                        channels=device_info.get(
                                            'maxInputChannels'),
                                        rate=self.RATE,
                                        input=True,
                                        frames_per_buffer=self.CHUNK_SIZE,
                                        input_device_index=device_info.get('index'))

        # connection loop
        while True:
            try:
                # get the data to send
                if(self.audio_stream):
                    data = self.audio_stream.read(self.CHUNK_SIZE)
                else:
                    data = None

                # send the data to the receiver
                self.sender_socket.sendto(
                    data, (receiver_address, receiver_port))
            except:  # break if there's an interruption in the data flow
                break
