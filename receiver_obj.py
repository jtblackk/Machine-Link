import socket
import pyaudio

class receiver:
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    p = pyaudio.PyAudio()


    # establish a socket connection with the sender module
    def connect_to_sender(self, sender_address, sender_port):
        # create a new socket
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to the sender
        self.sender_socket.connect((sender_address, sender_port))

    # streams audio from the receiver module to the sender module
    def receive_audio(self):
        # get header (number of channels to use)
        num_channels = self.sender_socket.recv(self.CHUNK_SIZE).decode('utf-8')


        # open audio stream
        self.audio_stream = self.p.open(format=self.FORMAT, 
                        channels=int(num_channels), 
                        rate=self.RATE,
                        output=True)

        # connection loop
        while True:
            try:
                # receive data from sender module
                received_data = self.sender_socket.recv(self.CHUNK_SIZE)
                
                if not received_data:
                    break

                # display the data (emit audio)
                self.audio_stream.write(received_data)
            except: # break if there's an interruption in the data flow
                break


    # close all of the connections involved in receiving audio
    def close_connection(self):
        # close socket and streams when connection broken
        self.sender_socket.close()
        try:
            self.audio_stream.stop_stream()
            self.audio_stream.close()
        except:
            pass
        self.p.terminate()



    