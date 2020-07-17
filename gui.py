# this is the front end of Unify.
# it will provide a gui to use the app.

import tkinter as tk
import receiver_obj as rcv_module
import sender_obj as snd_module
import threading





# create window object
window = tk.Tk()



    


# display the system's sending IP address + socket port
sender = snd_module.sender()
sender.create_sender_socket()
send_ip_label = tk.Label(text=f"this address: {sender.sender_address}").pack(anchor=tk.W)
send_port_label = tk.Label(text=f"this port: {sender.sender_port}").pack(anchor=tk.W)

# display the prompt for the receiver ip address
sender_address = tk.StringVar()
sender_port = tk.StringVar()
sender_address_label = tk.Label(text="Sender address:").pack(anchor=tk.W)
sender_address_input = tk.Entry(textvariable=sender_address).pack(anchor=tk.W)
sender_port_label = tk.Label(text="Sender port:").pack(anchor=tk.W)
sender_port_input = tk.Entry(textvariable=sender_port).pack(anchor=tk.W)

def connect_to_receiver():
    #TODO: ALLOW USER TO SELECT A RECEIVER THROUGH GUI
    # get audio source
    for device_index in range(0, sender.p.get_device_count()):
        device_info = sender.p.get_device_info_by_index(device_index)
        device_name = device_info.get("name")
        if str(device_name).count("Virtual") or str(device_name).count("Mic") or str(device_name).count("Stereo"):
            print(f"\t{device_index}: {device_name}")
    print("enter the id number of an audio device:")
    audio_device = int(input())

    sender.establish_connection()
    # sender.stream_audio(audio_device)
    stream_send_thread = threading.Thread(target=sender.stream_audio)
    stream_send_thread.start(audio_device)

def connect_to_sender():
    # instantiate receiver
    receiver = rcv_module.receiver()

    # get sender address and port
    sender_addr = sender_address.get()
    sender_prt = int(sender_port.get())

    # connect to the sender
    receiver.connect_to_sender(sender_addr, sender_prt)
    stream_receive_thread = threading.Thread(target=receiver.receive_audio)
    stream_receive_thread.start()

# display connect to receiver / listen for sender button
connect_to_rec_button = tk.Button(text="Receive Audio", command=connect_to_sender).pack(anchor=tk.W)
listen_for_sender_button = tk.Button(text="Send Audio", command=connect_to_receiver).pack(anchor=tk.W)

# render window
window.mainloop()

