from tkinter import *
from time import *
import json
import pathlib
from  profile import *
from  test import *



def log_out(main_interface_window):
    main_interface_window.destroy()
    main()

def main_interface(Username,Password):
    main_interface_window = Tk()
    main_interface_window.geometry("400x300")
    main_interface_window.title("Application")

    B = Button(main_interface_window, text ="add profile", command = lambda : menu(main_interface_window,1,Username,Password))
    B.place(x = 15, y = 10)

    B2 = Button(main_interface_window, text ="Log out", command = lambda : log_out(main_interface_window))
    B2.place(x = 320, y = 10)

    B3 = Button(main_interface_window, text ="add a Business card ", command = lambda : menu(0,Username,Password))
    B3.place(x = 130, y = 10)
    
    display_info(main_interface_window,Username,Password)
    main_interface_window.mainloop()