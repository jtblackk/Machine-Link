# this program is the audio capturer and emitter
# part of Unify. It's purpose is to capture audio
# from the system running the program, as well as
# emit audio to the speakers of the system running
# the program
import wave
import pyaudio


# pass in the location of the audio source (must be .wav)
# function plays the audio
def emit_audio_from_wav(wav_source):
    # open audio file
    sound = wave.open(wav_source, 'rb')

    # emit audio
    emit_audio(sound)


# emites audio from an audio source. 
def emit_audio(audio_source):
    # instantiate pyAudio
    p = pyaudio.PyAudio()

    # set stream settings
    FORMAT = p.get_format_from_width(audio_source.getsampwidth())
    CHUNK_SIZE = 1024
    CHANNELS = audio_source.getnchannels()
    RATE = audio_source.getframerate()

    # create stream
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

    # put audio into stream
    data = audio_source.readframes(CHUNK_SIZE)
    while data:
        stream.write(data) # play chunk
        data = audio_source.readframes(CHUNK_SIZE) # increment chunk

    # close stream and pyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

# def emit_audio_from_device(device):





