import socket
import pyaudio


class receiver:
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    p = pyaudio.PyAudio()

    # UDP, so no connection established. Just create a socket.
    def connect_to_sender(self, sender_address, sender_port):
        # create a new socket
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # streams audio from the receiver module to the sender module
    def receive_audio(self):
        # get header (number of channels to use)
        num_channels_bytes, sender_address = self.sender_socket.recvfrom(
            self.CHUNK_SIZE)
        num_channels = num_channels_bytes.decode('utf-8')

        # open audio stream
        self.audio_stream = self.p.open(format=self.FORMAT,
                                        channels=int(num_channels),
                                        rate=self.RATE,
                                        output=True)

        # connection loop
        while True:
            try:
                # receive data from sender module
                received_data, sender_address = self.sender_socket.recvfrom(
                    self.CHUNK_SIZE)

                if not received_data:
                    break

                # display the data (emit audio)
                self.audio_stream.write(received_data)
            except:  # break if there's an interruption in the data flow
                break
