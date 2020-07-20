# this is the front end of Unify.
# it will provide a gui to use the app.

import tkinter as tk
import receiver_obj as rec
import sender_obj as sen
import ipaddress as ip
import threading as td

class GUI:
    # declares class variables and builds ui
    def __init__(self, master):
        # ------ CLASS PROPERTIES SECTION ------ #
        self.master = master
        self.sender_module = sen.sender()
        self.receiver_module = rec.receiver()
        self.audio_source = tk.StringVar()
        self.audio_source.set("Choose a device")

        # ------ RECEIVE AUDIO SECTION ------ #
        # receiver section title
        receive_title = tk.Label(
                            master=self.master, 
                            text="Receive Audio")
        receive_title.grid(column=0, row=0, columnspan=2)

        # sender ip address form
        sender_ip_entry_label = tk.Label(
                                    master=self.master, 
                                    text="Sender IP:")
        sender_ip_entry_label.grid(column=0, row=1)
        sender_ip_entry = tk.Entry(
                                master=self.master)
        sender_ip_entry.grid(column=1, row=1)

        # sender port form
        sender_port_box_label = tk.Label(
                                    master=self.master, 
                                    text="Sender Port:")
        sender_port_box_label.grid(column=0, row=2)
        sender_port_box = tk.Entry(
                                master=self.master)
        sender_port_box.grid(column=1, row=2)

        # start receiving button
        receive_start_button = tk.Button(
                                    master=self.master, 
                                    text="Start", 
                                    command=self.start_receiver)
        receive_start_button.grid(column=0, row=3)

        # stop receiving button
        receive_stop_button = tk.Button(
                                    master=self.master, 
                                    text="Stop", 
                                    state=tk.DISABLED, 
                                    command=self.stop_receiver)
        receive_stop_button.grid(column=1, row=3)

        # receiver status
        receiver_status_label = tk.Label(
                                    master=self.master, 
                                    text="Status:")
        receiver_status_label.grid(column=0, row=4)
        receiver_status = tk.Label(
                                master=self.master, 
                                text="Off")
        receiver_status.grid(column=1, row=4)


        # ------ RECEIVE AUDIO SECTION ------ #
        # sender section title
        send_title = tk.Label(
                            master=self.master, 
                            text="Send Audio")
        send_title.grid(column=2, row=0, columnspan=2)

        # audio device form
        audio_device_label = tk.Label(
                                    master=self.master, 
                                    text="Stream from:")
        audio_device_label.grid(column=2, row=1)
        audio_device_selection = tk.OptionMenu(
                                            self.master, 
                                            self.audio_source, 
                                            self.audio_source.get(), 
                                            *(self.sender_module.get_audio_devices()))
        audio_device_selection.grid(column=3, row=1)

        # start stream button
        send_start_button = tk.Button(
                                    master=self.master, 
                                    text="Start", 
                                    command=self.start_sender)
        send_start_button.grid(column=2, row=3)

        # stop stream button
        send_stop_button = tk.Button(
                                master=self.master, 
                                text="Stop", 
                                state=tk.DISABLED, 
                                command=self.stop_sender)
        send_stop_button.grid(column=3, row=3)

        # sender status
        sender_status_label = tk.Label(
                                    master=self.master, 
                                    text="Status:")
        sender_status_label.grid(column = 2, row=4)
        sender_status = tk.Label(
                            master=self.master, 
                            text="Off")
        sender_status.grid(column=3, row=4)

        # stream address
        sender_address_label = tk.Label(
                                    master=self.master, 
                                    text="Stream Address:")
        sender_address_label.grid(column = 2, row=5)
        sender_address = tk.Label(
                            master=self.master, 
                            text="Unavailable")
        sender_address.grid(column=3, row=5)

    # callback function for when the user presses "start" on the receiver module
    def start_receiver(self):
        print("start_receiver()")

    # callback function for when the user presses "stop" on the receiver module
    def stop_receiver(self):
        print("stop_receiver()")

    # callback function for when the user presses "start" on the sender module
    def start_sender(self):
        print("start_sender()")

    # callback function for when the user presses "stop" on the sender module
    def stop_sender(self):
        print("stop_sender()")