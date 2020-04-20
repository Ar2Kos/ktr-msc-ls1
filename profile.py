from tkinter import *
from time import *
import json
import pathlib

def error_wd():
    error_window = Tk()
    error_window.geometry("200x100")
    error_window.title("error")
    txtname = Label(error_window, text="Invalid Input").place(x = 80, y = 25)
    B = Button(error_window, text ="Exit",highlightbackground='#3E4149', command = lambda : error_window.destroy())
    B.place(x = 80, y = 60)


def display_info(main_interface_window,Username,Password):
    filename = "app.json"
    found = False
    info = []
    # Writing JSON data
    with open(filename) as f:
        data = json.load(f)
        for conn in data["connexion"]:
            if(conn["Username"] == Username and conn["Password"] == Password and 'name' in conn.keys()):
                info = conn
                xtname = Label(main_interface_window, text="test").place(x = 20, y = 50)
                break
    if not info:
        msg = Label(main_interface_window, text="It seems you do not have a profile yet").place(x = 40, y = 55)
    else:
        fraude = Label(main_interface_window, text="                                                                   ").place(x = 40, y = 55)
        xtname = Label(main_interface_window, text="Name :      " + info["name"]).place(x = 20, y = 50)
        txtC_name = Label(main_interface_window, text="Company name :      "+ info["C_name"]).place(x = 20, y = 75)
        txtemail = Label(main_interface_window, text="Email address :      "+ info["Email"]).place(x = 20, y = 100)
        txttel = Label(main_interface_window, text="Telephone number :      "+ info["Telephone"]).place(x = 20, y = 125)


def add_new_profile(main_interface_window,interface_window,name,C_name,Email,Telephone,Username,Password):
    filename = "app.json"
    dataset = []
    with open(filename, 'r') as f:
        data = json.load(f)
        dataset = data
    for i in range(len(dataset["connexion"] )):
        if(dataset["connexion"][i]["Username"] == Username and dataset["connexion"][i]["Password"] == Password):
            del dataset["connexion"][i]
            break
    with open(filename, 'w') as f:
        dataset["connexion"].append({
                'Username': Username,
                'Password': Password,
                'name' : name,
                'C_name' : C_name,
                'Email' : Email,
                'Telephone' : Telephone
                })
        json.dump(dataset, f)
    interface_window.destroy()
    display_info(main_interface_window,Username,Password)


def store_data(interface_window,name,C_name,Email,Telephone,Username,Password):
    if (name == "" or C_name ==""  or Email == "" or Telephone == ""):
        error_wd()
    else:
        datastore = {
            'name' : name,
            'C_name' : C_name,
            'Email' : Email,
            'Telephone' : Telephone
        }
        filename = "app.json"

        # If the file name exists, write a JSON string into the file.
        if filename:
            with open(filename) as f:
                dic = json.load(f)
                dic["info"].append(datastore)
                with open(filename, 'w') as f:
                    json.dump(dic, f)
        interface_window.destroy()
    
def store_or_add_new(main_interface_window,switch,interface_window,name,C_name,Email,Telephone,Username,Password):
    if(switch == 1):
        add_new_profile(main_interface_window,interface_window,name,C_name,Email,Telephone,Username,Password)
    else:
        store_data(interface_window,name,C_name,Email,Telephone,Username,Password)

def menu(main_interface_window,switch,Username,Password):
    interface_window = Toplevel()
    interface_window.geometry("300x180")
    interface_window.title("profile")
    txtname = Label(interface_window, text="Name :").place(x = 20, y = 25)
    name = Entry(interface_window)
    name.place(x = 150, y = 25)
    
    txtC_name = Label(interface_window, text="Company name :").place(x = 20, y = 50)
    C_name = Entry(interface_window)
    C_name.place(x = 150, y = 50)
    
    txtemail = Label(interface_window, text="Email address :").place(x = 20, y = 75)
    Email = Entry(interface_window)
    Email.place(x = 150, y = 75)

    txttel = Label(interface_window, text="Telephone number :").place(x = 20, y = 100)
    Telephone = Entry(interface_window)
    Telephone.place(x = 150, y = 100)

    B = Button(interface_window, text ="add info", command = lambda : store_or_add_new(main_interface_window,switch,interface_window,name.get(),C_name.get(),Email.get(),Telephone.get(),Username,Password))
    B.place(x = 77, y = 130)
