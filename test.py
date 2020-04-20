from tkinter import *
from time import *
import json
import pathlib
from  profile import *
from  main_interface import *
 
 
def error_conn():
    error_window = Tk()
    error_window.geometry("200x100")
    error_window.title("error")
    txtname = Label(error_window, text="Unknow User or wrong password").place(x = 10, y = 25)
    B = Button(error_window, text ="Exit",highlightbackground='#3E4149', command = lambda : error_window.destroy())
    B.place(x = 80, y = 60)


def check_connexion(main_window,Username,Password):
    if (Username == "" or Password =="" ):
        error_wd()
    else:
        filename = "app.json"
        found = False
        # If the file name exists, write a JSON string into the file.
        if filename:
            # Writing JSON data
            with open(filename) as f:
                data = json.load(f)
            for conn in data["connexion"]:
                if(conn["Username"] == Username and conn["Password"] == Password):
                    main_interface(Username,Password)
                    main_window.destroy()
                    found = True
            if(not(found)):
                error_conn()

def create_User(main_window,Username,Password):
    if (Username == "" or Password =="" ):
        error_wd()
    else:
        filename = "app.json"
        """hash = 31
        for i in range(Password.len()):
            hash = hash*7 + Password.charAt(i)
        """
        datastore  = {
            'Username': Username,
            #'Password': hash(Password)
            'Password': Password
        }
        # If the file name exists, write a JSON string into the file.
        if filename:
            # Writing JSON data
            with open(filename) as f:
                dic = json.load(f)
            dic["connexion"].append(datastore)
            with open(filename, 'w') as f:
                json.dump(dic, f)
        main_window.destroy()
        main_interface(Username,Password)
        

def setup_jsonfile():
    setup = {}
    setup["info"] = []
    setup["connexion"] = []
    with open('app.json', 'a') as f:
            json.dump(setup, f)

def main():
    if(not(pathlib.Path('app.json').exists())):
        setup_jsonfile()

    main_window = Tk()
    main_window.geometry("300x100")
    main_window.title("Login")
    txtUsername = Label(main_window, text="Username :").place(x = 20, y = 20)
    Username = Entry(main_window)
    Username.place(x = 90, y = 20)
    
    txtPassword = Label(main_window, text="Password :").place(x = 20, y = 40)
    Password = Entry(main_window)
    Password.place(x = 90, y = 40)

    B = Button(main_window, text ="Enter", command = lambda : check_connexion(main_window,Username.get(),Password.get()))
    B.place(x = 90, y = 65)

    B2 = Button(main_window, text ="Sign up", command = lambda : create_User(main_window,Username.get(),Password.get()))
    B2.place(x = 160, y = 65)
    main_window.mainloop()


if __name__ == '__main__':
    main()