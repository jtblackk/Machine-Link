import socket
import pyaudio

class receiver:
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    p = pyaudio.PyAudio()


    # establish a socket connection with the sender module
    # preconditions: 
    #   1. sender_address (ip address of sender module) is attained
    #   2. sender_port (port of the sender module) is attained
    # postconditions:
    #   1. self.sender_socket will be a socket connection to the sender module
    def connect_to_sender(self, sender_address, sender_port):
        # create a new socket
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to the sender
        self.sender_socket.connect((sender_address, sender_port))
        print("connected to sender")

    # streams audio from the receiver module to the sender module
    # preconditions:
    #   1. receiver has connected to the sender
    # postconditions:
    #   1. socket will be closed
    def receive_audio(self):
        # get header (number of channels to use)
        num_channels = self.sender_socket.recv(self.CHUNK_SIZE).decode('utf-8')


        # open audio stream
        self.audio_stream = self.p.open(format=self.FORMAT, 
                        channels=int(num_channels), 
                        rate=self.RATE,
                        output=True)

        # connection loop
        while not self.sender_socket.fileno() == -1:
            # receive data from sender module
            received_data = self.sender_socket.recv(self.CHUNK_SIZE)
            
            # break if kill message
            if not received_data:
                break

            # display the data (emit audio)
            self.audio_stream.write(received_data)

    # closes all of the connections involved in streming
    def close_connection(self):
        # close socket and streams when connection broken
        self.sender_socket.close()
        self.audio_stream.stop_stream()
        self.audio_stream.close()
        self.p.terminate()



    