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
        self.receive_title = tk.Label(
                            master = self.master, 
                            text = "Receive Audio")
        self.receive_title.grid(column = 0, row = 0, columnspan = 2)

        # sender ip address form
        self.sender_ip_label = tk.Label(
                                    master = self.master, 
                                    text = "Sender IP:")
        self.sender_ip_label.grid(column = 0, row = 1, sticky = tk.E)
        self.sender_ip_entry = tk.Entry(
                                master = self.master,
                                width = 14)
        self.sender_ip_entry.grid(column = 1, row = 1, sticky = tk.W)

        # sender port form
        self.sender_port_label = tk.Label(
                                    master = self.master, 
                                    text = "Sender Port:")
        self.sender_port_label.grid(column = 0, row = 2, sticky = tk.E)
        self.sender_port_entry = tk.Entry(
                                master = self.master,
                                width = 4)
        self.sender_port_entry.grid(column = 1, row = 2, sticky = tk.W)

        # start receiving button
        self.receive_start_button = tk.Button(
                                    master = self.master, 
                                    text = "Start",
                                    width = 5, 
                                    command = self.start_receiver)
        self.receive_start_button.grid(column = 1, row = 3, sticky = tk.W)

        # stop receiving button
        self.receive_stop_button = tk.Button(
                                    master = self.master, 
                                    text = "Stop",
                                    width = 5, 
                                    state = tk.DISABLED, 
                                    command = self.stop_receiver)
        self.receive_stop_button.grid(column = 1, row = 4, sticky = tk.W)

        # receiver status
        self.receiver_status_label = tk.Label(
                                    master = self.master, 
                                    text = "Status:")
        self.receiver_status_label.grid(column = 0, row = 5, sticky = tk.E)
        self.receiver_status = tk.Label(
                                master = self.master, 
                                text = "Off")
        self.receiver_status.grid(column = 1, row = 5, sticky = tk.W)


        # ------ SEND AUDIO SECTION ------ #
        # sender section title
        self.send_title = tk.Label(
                            master = self.master, 
                            text = "Send Audio")
        self.send_title.grid(column = 2, row = 0, columnspan = 2)

        # audio device form
        self.audio_device_label = tk.Label(
                                    master = self.master, 
                                    text = "Stream from:")
        self.audio_device_label.grid(column = 2, row = 1, sticky = tk.E)
        self.audio_device_selection = tk.OptionMenu(
                                            self.master, 
                                            self.audio_source, 
                                            self.audio_source.get(), 
                                            *(self.sender_module.get_audio_devices()))
        self.audio_device_selection.grid(column = 3, row = 1)

        # start stream button
        self.send_start_button = tk.Button(
                                    master = self.master, 
                                    text = "Start", 
                                    width = 5,
                                    command = self.start_sender)
        self.send_start_button.grid(column = 3, row = 3, sticky = tk.W)

        # stop stream button
        self.send_stop_button = tk.Button(
                                master = self.master, 
                                text = "Stop", 
                                width = 5,
                                state = tk.DISABLED, 
                                command = self.stop_sender)
        self.send_stop_button.grid(column = 3, row = 4, sticky = tk.W)

        # sender status
        self.sender_status_label = tk.Label(
                                    master = self.master, 
                                    text = "Status:")
        self.sender_status_label.grid(column = 2, row = 5, sticky = tk.E)
        self.sender_status_text = tk.Label(
                            master = self.master, 
                            text = "Off")
        self.sender_status_text.grid(column = 3, row = 5, sticky = tk.W)

        # stream address
        self.sender_address_label = tk.Label(
                                    master = self.master, 
                                    text = "Sender Address:")
        self.sender_address_label.grid(column = 2, row = 6, sticky = tk.E)
        self.sender_address_text = tk.Label(
                            master = self.master, 
                            text = "Unavailable")
        self.sender_address_text.grid(column = 3, row = 6, sticky = tk.W)

    # callback function for when the user presses "start" on the receiver module
    def start_receiver(self):
        print("start_receiver()")
        # validate ip address entry
        try:
            ip.ip_address(self.sender_ip_entry.get())
        except ValueError:
            self.receiver_status['text'] = "Invalid address"
            self.receiver_status['fg'] = "red"
            return
        
        # validate port entry
        if not self.sender_port_entry.get().isdigit():
            self.receiver_status['text'] = "Invalid Port"
            self.receiver_status['fg'] = "red"

        # switch start/stop button states
        self.receive_start_button['state'] = tk.DISABLED
        self.receive_stop_button['state'] = tk.ACTIVE

        # establish connection with sender
        self.receiver_status['text'] = "Connecting"
        self.receiver_status['fg'] = "orange"
        self.receiver_module.connect_to_sender(self.sender_ip_entry.get(), int(self.sender_port_entry.get()))
        self.receiver_status['text'] = "Connected"
        self.receiver_status['fg'] = "green"

    # callback function for when the user presses "stop" on the receiver module
    def stop_receiver(self):
        print("stop_receiver()")

    # callback function for when the user presses "start" on the sender module
    def start_sender(self):
        print("start_sender()")

    # callback function for when the user presses "stop" on the sender module
    def stop_sender(self):
        print("stop_sender()")