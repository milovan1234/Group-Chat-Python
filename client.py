import tkinter
from tkinter import *
from tkinter import messagebox
from models import ClientManager
from models import User
import threading

LOGIN_USER_USERNAME = ''
SOCK_LOGIN = ''

#POCETNA FORMA
def FormStart():
    root = tkinter.Tk()
    root.title("Start Form")
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - 150
    y = (heightScreen / 2) - 150
    root.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    frameLogReg = Frame(root)
    frameLogReg.place(in_=root, anchor="c", relx=0.5, rely=0.5)

    lblTitle = Label(frameLogReg, text="Group Chat Application", font=("Times", "17"))
    lblTitle.pack(pady=20)

    # dugme za otvaranje login forme
    btnOpenLogin = Button(frameLogReg, text="LOGIN", command=lambda: OpenLogin(root))
    btnOpenLogin.pack(pady=5)

    # dugme za otvaranje register forme
    btnOpenRegister = Button(frameLogReg, text="REGISTER", command=lambda: OpenRegister(root))
    btnOpenRegister.pack(pady=5)

    root.mainloop()

#Prelazak na formu za logovanje sa pocetne forme
def OpenLogin(root):
    root.destroy()
    FormLogin()

#Prelazak na formu za registraciju sa pocetne forme
def OpenRegister(root):
    root.destroy()
    FormRegister()



#FORM ZA LOGOVANJE
def FormLogin():
    root = tkinter.Tk()
    root.title("Login Form")
    # centriranje forme na sredini ekrana
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - 150
    y = (heightScreen / 2) - 150
    root.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    frameLogin = Frame(root)
    frameLogin.place(in_=root, anchor="c", relx=0.5, rely=0.5)

    lblLoginTitle = Label(frameLogin, text="Login", font=("Times", "15"))
    lblLoginTitle.pack(pady=15)

    frameUsername = Frame(frameLogin)
    frameUsername.pack(pady=5)
    lblUsername = Label(frameUsername, text="Username: ")
    lblUsername.pack(side=LEFT)
    txtUsername = Entry(frameUsername)
    txtUsername.pack()

    framePassword = Frame(frameLogin)
    framePassword.pack(pady=5)
    lblPassword = Label(framePassword, text="Password: ")
    lblPassword.pack(side=LEFT)
    txtPassword = Entry(framePassword, show="•")
    txtPassword.pack()

    btnLoginSubmit = Button(frameLogin, text="LOGIN", command=lambda: LoginSubmit(txtUsername.get(), txtPassword.get(), root))
    btnLoginSubmit.pack(anchor=W, pady=10)

    btnBackToStart = Button(frameLogin, text="START FROM", command=lambda: LoginToStart(root))
    btnBackToStart.pack(anchor=W)
    root.mainloop()

#Funkcija za povratak na pocetnu formu iz forme za logovanje
def LoginToStart(root):
    root.destroy()
    FormStart()

#Slanje podataka za prijavljivanje
def LoginSubmit(username, password,root):
    global LOGIN_USER_USERNAME
    global SOCK_LOGIN
    if username == "" or password == "":
        messagebox.showwarning("Greska pri unosu", "Sva polja moraju biti popunjena!")
    else:
        result, SOCK_LOGIN = ClientManager.ClientLogin(username,password)
        if result == "Error":
            messagebox.showwarning("Prijava", "Uneseni podaci nisu ispravni!")
        elif result == "Exist":
            messagebox.showwarning("Prijava", "Korisnik je vec prijavljen sa unetim podacima!")
        else:
            messagebox.showinfo("Prijava", "Uspesno ste se prijavili!")
            LOGIN_USER_USERNAME = result
            LoginToUser(root)

def LoginToUser(root):
    root.destroy()
    FormUser()

#FORM ZA REGISTRACIJU
def FormRegister():
    root = tkinter.Tk()
    root.title("Register Form")
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - 150
    y = (heightScreen / 2) - 150
    root.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    frameRegister = Frame(root)
    frameRegister.place(in_=root, anchor="c", relx=0.5, rely=0.5)

    lblRegisterTitle = Label(frameRegister, text="Register", font=("Times", "15"))
    lblRegisterTitle.pack(pady=15)

    frameFirstname = Frame(frameRegister)
    frameFirstname.pack(pady=5)
    lblFirstname = Label(frameFirstname, text="First name: ")
    lblFirstname.pack(side=LEFT)
    txtFirstname = Entry(frameFirstname)
    txtFirstname.pack()

    frameLastname = Frame(frameRegister)
    frameLastname.pack(pady=5)
    lblLastname = Label(frameLastname, text="Last name: ")
    lblLastname.pack(side=LEFT)
    txtLastname = Entry(frameLastname)
    txtLastname.pack()

    frameUsername = Frame(frameRegister)
    frameUsername.pack(pady=5)
    lblUsername = Label(frameUsername, text="Username: ")
    lblUsername.pack(side=LEFT)
    txtUsername = Entry(frameUsername)
    txtUsername.pack()

    framePassword = Frame(frameRegister)
    framePassword.pack(pady=5)
    lblPassword = Label(framePassword, text="Password: ")
    lblPassword.pack(side=LEFT)
    txtPassword = Entry(framePassword, show="•")
    txtPassword.pack()

    btnRegisterSubmit = Button(frameRegister, text="REGISTER", command=lambda: RegisterSubmit(txtFirstname.get(),txtLastname.get(),
                                                                                              txtUsername.get(),txtPassword.get()))
    btnRegisterSubmit.pack(anchor=W, pady=10)

    btnBackToStart = Button(frameRegister, text="START FROM", command=lambda: RegisterToStart(root))
    btnBackToStart.pack(anchor=W)

    root.mainloop()

#Slanje podataka za registraciju
def RegisterSubmit(firstname,lastname,username,password):
    if firstname == "" or lastname == "" or username == "" or password == "":
        messagebox.showwarning("Greska pri unosu", "Sva polja moraju biti popunjena!")
    else:
        if ClientManager.ClientRegister(firstname,lastname,username,password):
            messagebox.showinfo("Registracija", "Uspesno ste se registrovali. Idite na formu za Prijavu!")
        else:
            messagebox.showwarning("Registracija", "Uneseni username je vec zauzet!")

#Funkcija za povratak na pocetnu formu iz forme za registraciju
def RegisterToStart(root):
    root.destroy()
    FormStart()


def FormUser():
    root = tkinter.Tk()
    root.title("User Form")
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - 250
    y = (heightScreen / 2) - 250
    root.geometry('%dx%d+%d+%d' % (500, 500, x, y))

    user = ClientManager.ClientGetData(LOGIN_USER_USERNAME)

    lblUsername = Label(root, text="USER:" + user.firstname + " " + user.lastname, font=("Times", "15"))
    lblUsername.pack(pady=20)

    btnLogout = Button(root,text="LOGOUT", command=lambda: LogoutUser(root))
    btnLogout.pack()

    root.protocol("WM_DELETE_WINDOW", lambda: FormUserClosing(root))
    root.mainloop()

def FormUserClosing(root):
    if messagebox.askokcancel("Odjava", "Da li ste sigurni da zelite da se odjavite?"):
        LogoutUser(root)

def LogoutUser(root):
    if ClientManager.ClientLogout(LOGIN_USER_USERNAME):
        root.destroy()
        FormStart()




FormStart()


