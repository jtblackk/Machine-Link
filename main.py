# main function for Unify.
# Runs the TkInter window

from gui_obj import *

if __name__ == "__main__":
    master = tk.Tk()
    master.title("Unify")
    master.iconbitmap('assets/unify_icon_x7I_icon.ico')
    window = GUI(master)
    master.mainloop()