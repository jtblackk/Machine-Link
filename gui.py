# this is the front end of Unify.
# it will provide a gui to use the app.

import tkinter as tk


# create window object
window = tk.Tk()


# display greeting
greeting = tk.Label(text="howdie uwu").pack()

# display sender/receiver radio buttons
program_mode = str()
button = tk.Radiobutton(text="Sender", 
                variable="program_node", 
                value="sender"
            ).pack(anchor=tk.W)

button2= tk.Radiobutton(text="Receiver", 
                variable="program_node", 
                value="receiver"
            ).pack(anchor=tk.W)


# render window
window.mainloop()
