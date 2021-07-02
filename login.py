from tkinter import *
import sqlite3

root = Tk()
root.title("Moithuti: Login")
width = 500
height = 480
screen_bg = " blue"
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("moithuti.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `user` (id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, Fullnames , Password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `Fullnames` = 'admin' AND `Password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (Fullnames, Password) VALUES('admin', 'admin')")
        conn.commit()
def Login(event=None):
    Database()


    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()

def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Moithuti: Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfull Login!", font=('Century Gothic', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

def Back():
    Home.destroy()
    root.deiconify()
    
#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()

#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text = "Python: Moithuti", font=('Calibri', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('Calibri', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('Calibri', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=35, row=5, columnspan=2)
btn_login.bind('<Return>', Login)
