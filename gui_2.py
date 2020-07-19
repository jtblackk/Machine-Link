import tkinter as tk
import receiver_obj as rec
import sender_obj as sen
import ipaddress
import threading

CONNECTION_TIMEOUT = 10


# callback function to start the receiver
def start_receiver():
    # validate entered IP address
    try:
        ipaddress.ip_address(sender_ip_box.get())
    except ValueError:
        receiver_status['text'] = "Invalid address"
        receiver_status['fg'] = "red"
        return

    # validate entered port
    if not str(sender_port_box.get()).isdigit():
        receiver_status['text'] = "Invalid port"
        receiver_status['fg'] = "red"
        return

    # toggle start/stop button states and update status
    receive_start_button['state'] = tk.DISABLED
    receive_stop_button['state'] = tk.ACTIVE
    receiver_status['text'] = "Connecting"
    receiver_status['fg'] = "orange"

    # establish socket connection with receiver
    # TODO: move this to another thread. currently causes program to hang.
    receiver.connect_to_sender(sender_ip_box.get(), int(sender_port_box.get()))

    # update status
    receiver_status['text'] = "Connected"
    receiver_status['fg'] = "green"

    # start receiving audio
    # TODO: move function to another thread. currently causes program to hang.
    receiver.receive_audio()



# callback function to stop the receiver
def stop_receiver():
    # toggle start/stop button states
    receive_start_button['state'] = tk.ACTIVE
    receive_stop_button['state'] = tk.DISABLED

    # update status
    receiver_status['text'] = "Disconnected"
    receiver_status['fg'] = "black"

    receiver.close_connection()


# callback function to start the sender
def start_sender(): 
    # toggle start/stop button states
    send_start_button['state'] = tk.DISABLED
    send_stop_button['state'] = tk.ACTIVE

    # update status
    sender_status['text'] = "Connecting"
    sender_status['fg'] = "orange"

    # establish a connection
    # TODO: move function to another thread
    sender.establish_connection()

    # update status
    sender_status['text'] = "Connected"
    sender_status['fg'] = "green"

    # start streaming audio
    # TODO: move function to another thread
    sender.stream_audio(chosen_item.get())

    # update status
    sender_status['text'] = "Streaming"
    sender_status['fg'] = "green"

# callback function to stop the sender
def stop_sender():
    # toggle start/stop button states
    send_start_button['state'] = tk.ACTIVE
    send_stop_button['state'] = tk.DISABLED
    
    # update status
    sender_status['text'] = "Disconnected"
    sender_status['fg'] = "black"





# win = tk.Toplevel()
root = tk.Tk()

# instantiate sender and receiver
sender = sen.sender()
receiver = rec.receiver()




# ------ RECEIVE AUDIO SECTION ------ #
# receiver section title
receive_title = tk.Label(
                        master=root, 
                        text="Receive Audio"
                    ).grid(
                        column=0, 
                        row=0, 
                        columnspan=2)


# form to enter address of a sender to connect to
sender_ip_box_label = tk.Label(
                            master=root, 
                            text="Sender IP:"
                        ).grid(
                            column=0, 
                            row=1)

sender_ip_box = tk.Entry(
                        master=root
                    )
sender_ip_box.grid(
                column=1, 
                row=1)

sender_port_box_label = tk.Label(
                            master=root, 
                            text="Sender Port:"
                        ).grid(
                            column=0, 
                            row=2)

sender_port_box = tk.Entry(
                        master=root
                    )
sender_port_box.grid(
                    column=1, 
                    row=2)


# buttons to start and stop connection to a sender
receive_start_button = tk.Button(
                            master=root, 
                            text="Start", 
                            command=start_receiver)
receive_start_button.grid(
                        column=0, 
                        row=3)

receive_stop_button = tk.Button(
                            master=root, 
                            text="Stop", 
                            state=tk.DISABLED, 
                            command=stop_receiver)
receive_stop_button.grid(
                        column=1, 
                        row=3)


# status of receiver (unconnected, connected)
receiver_status_label = tk.Label(
                            master=root, 
                            text="Status:"
                        ).grid(
                            column=0, 
                            row=4)

receiver_status = tk.Label(
                        master=root, 
                        text="Off"
                    )
receiver_status.grid(
                    column=1, 
                    row=4)




# ------ SEND AUDIO SECTION ------ #
# sender section title
send_title = tk.Label(
                    master=root, 
                    text="Send Audio"
                ).grid(
                    column=2, 
                    row=0, 
                    columnspan=2)


# form to select audio device to stream from
audio_device_selection_label = tk.Label(
                                    master=root, 
                                    text="Stream from:"
                                ).grid(
                                    column=2, 
                                    row=1)

audio_device_options = sender.get_audio_devices()
chosen_item = tk.StringVar()
chosen_item.set("Choose a device")
audio_device_selection = tk.OptionMenu(
                                    root, 
                                    chosen_item, 
                                    "Choose a device", 
                                    *audio_device_options
                                )
audio_device_selection.grid(
                            column=3, 
                            row=1)


# buttons to stop and start audio stream
send_start_button = tk.Button(
                            master=root, 
                            text="Start", 
                            command=start_sender)
send_start_button.grid(
                    column=2, 
                    row=3)

send_stop_button = tk.Button(
                        master=root, 
                        text="Stop", 
                        state=tk.DISABLED, 
                        command=stop_sender)
send_stop_button.grid(
                    column=3, 
                    row=3)


# status of sender (off/waiting for connection/connected); (show ip address if waiting for a connection)
sender_status_label = tk.Label(
                            master=root, 
                            text="Status:"
                        ).grid(
                            column = 2, 
                            row=4)

sender_status = tk.Label(
                        master=root, 
                        text="<sender status>"
                    )
sender_status.grid(
                column=3, 
                row=4)

sender_address_label = tk.Label(
                            master=root, 
                            text="Sender Address:"
                        ).grid(
                            column = 2, 
                            row=5)

sender_ip = tk.Label(
                    master=root, 
                    text="<sender ip : sender port>"
                ).grid(
                    column=3, 
                    row=5)




tk.mainloop()