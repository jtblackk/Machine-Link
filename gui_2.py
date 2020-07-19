import tkinter as tk
import receiver_obj as rec
import sender_obj as sen


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
sender_ip_box_label = tk.Label(master=root, text="Sender IP:").grid(column=0, row=1)
sender_ip_box = tk.Entry(master=root).grid(column=1, row=1)

sender_port_box_label = tk.Label(master=root, text="Sender Port:").grid(column=0, row=2)
sender_port_box = tk.Entry(master=root).grid(column=1, row=2)

# buttons to start and stop connection to a sender
receive_start_button = tk.Button(master=root, text="Start").grid(column=0, row=3)
receive_stop_button = tk.Button(master=root, text="Stop").grid(column=1, row=3)

# status of receiver (unconnected, connected)
receiver_status_label = tk.Label(master=root, text="Status:").grid(column = 0, row=4)
receiver_status = tk.Label(master=root, text="<receiver status>").grid(column=1, row=4)




# ------ SEND AUDIO SECTION ------ #
# sender section title
send_title = tk.Label(master=root, text="Send Audio").grid(column=2, row=0, columnspan=2)

# form to select audio device to stream from
audio_device_selection_label = tk.Label(master=root, text="Stream from:").grid(column=2, row=1)
audio_device_options = sender.get_audio_devices()
chosen_item = tk.StringVar()
chosen_item.set("Choose a device")
audio_device_selection = tk.OptionMenu(root, chosen_item, "Choose a device", *audio_device_options).grid(column=3, row=1)

# buttons to stop and start audio stream
sender_start_button = tk.Button(master=root, text="Start").grid(column=2, row=3)
sender_stop_button = tk.Button(master=root, text="Stop").grid(column=3, row=3)

# status of sender (off/waiting for connection/connected); (show ip address if waiting for a connection)
sender_status_label = tk.Label(master=root, text="Status:").grid(column = 2, row=4)
sender_status = tk.Label(master=root, text="<sender status>").grid(column=3, row=4)
sender_address_label = tk.Label(master=root, text="Sender Address:").grid(column = 2, row=5)
sender_ip = tk.Label(master=root, text="<sender ip : sender port>").grid(column=3, row=5)

tk.mainloop()