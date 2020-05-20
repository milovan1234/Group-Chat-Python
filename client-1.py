import tkinter
from tkinter import *
from tkinter import messagebox
from models import ClientManager
from models import User
import threading

LOGIN_USER_USERNAME = ''

#POCETNA FORMA
def FormStart():
    root = tkinter.Tk()
    root.configure(background="#343a40")
    root.title("Start Form")
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - 150
    y = (heightScreen / 2) - 150
    root.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    frameLogReg = Frame(root)
    frameLogReg.configure(background="#343a40")
    frameLogReg.place(in_=root, anchor="c", relx=0.5, rely=0.5)

    lblTitle = Label(frameLogReg, text="Group Chat Application", font=("Times", "17"), fg="#1a8cff", bg="#343a40")
    lblTitle.pack(pady=20)

    # dugme za otvaranje login forme
    btnOpenLogin = Button(frameLogReg, text="LOGIN", command=lambda: OpenLogin(root), width=10)
    btnOpenLogin.pack(pady=5)

    # dugme za otvaranje register forme
    btnOpenRegister = Button(frameLogReg, text="REGISTER", command=lambda: OpenRegister(root),width=10)
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
    root.configure(background="#343a40")
    # centriranje forme na sredini ekrana
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - 150
    y = (heightScreen / 2) - 150
    root.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    frameLogin = Frame(root)
    frameLogin.place(in_=root, anchor="c", relx=0.5, rely=0.5)
    frameLogin.configure(background="#343a40")

    lblLoginTitle = Label(frameLogin, text="Login", font=("Times", "16"), fg="#1a8cff", bg="#343a40")
    lblLoginTitle.pack(pady=15)

    frameUsername = Frame(frameLogin)
    frameUsername.pack(pady=5)
    frameUsername.configure(background="#343a40")
    lblUsername = Label(frameUsername, text="Username: ", fg="white",bg="#343a40", font=("Arial", "10"))
    lblUsername.pack(side=LEFT)
    txtUsername = Entry(frameUsername, font=("Arial", "10"))
    txtUsername.pack()

    framePassword = Frame(frameLogin)
    framePassword.pack(pady=5)
    framePassword.configure(background="#343a40")
    lblPassword = Label(framePassword, text="Password: ", fg="white",bg="#343a40", font=("Arial", "10"))
    lblPassword.pack(side=LEFT)
    txtPassword = Entry(framePassword, show="•", font=("Arial", "10"))
    txtPassword.pack()

    #Dugme za slanje podataka o korisnickom imenu i lozinki prilikom prijave
    btnLoginSubmit = Button(frameLogin, text="LOGIN", command=lambda: LoginSubmit(txtUsername.get(), txtPassword.get(), root), width=12)
    btnLoginSubmit.pack(anchor=W, pady=15)

    #Dugme za povratak na pocetnu formu aplikacije
    btnBackToStart = Button(frameLogin, text="START FROM", command=lambda: LoginToStart(root), width=12)
    btnBackToStart.pack(anchor=W)
    root.mainloop()

#Funkcija za povratak na pocetnu formu iz forme za logovanje
def LoginToStart(root):
    root.destroy()
    FormStart()

#Slanje podataka za prijavljivanje
def LoginSubmit(username, password,root):
    global LOGIN_USER_USERNAME
    if username == "" or password == "":
        messagebox.showwarning("Greska pri unosu", "Sva polja moraju biti popunjena!")
    else:
        result = ClientManager.ClientLogin(username,password)
        if result == "Error":
            messagebox.showwarning("Prijava", "Uneseni podaci nisu ispravni!")
        elif result == "Exist":
            messagebox.showwarning("Prijava", "Korisnik je vec prijavljen sa unetim podacima!")
        else:
            messagebox.showinfo("Prijava", "Uspesno ste se prijavili!")
            LOGIN_USER_USERNAME = result
            LoginToUser(root)

#Funckija za prelazak na korisnicku formu prilikom uspesne prijave
def LoginToUser(root):
    root.destroy()
    FormUser()

#FORM ZA REGISTRACIJU
def FormRegister():
    root = tkinter.Tk()
    root.title("Register Form")
    root.configure(background="#343a40")
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - 170
    y = (heightScreen / 2) - 170
    root.geometry('%dx%d+%d+%d' % (340, 340, x, y))

    frameRegister = Frame(root)
    frameRegister.place(in_=root, anchor="c", relx=0.5, rely=0.5)
    frameRegister.configure(background="#343a40")

    lblRegisterTitle = Label(frameRegister, text="Register", font=("Times", "16"), fg="#1a8cff", bg="#343a40")
    lblRegisterTitle.pack(pady=15)

    frameFirstname = Frame(frameRegister)
    frameFirstname.pack(pady=5)
    frameRegister.configure(background="#343a40")
    lblFirstname = Label(frameFirstname, text="First name: ", fg="white", bg="#343a40", font=("Arial", "10"))
    lblFirstname.pack(side=LEFT)
    txtFirstname = Entry(frameFirstname, font=("Arial", "10"))
    txtFirstname.pack()

    frameLastname = Frame(frameRegister)
    frameLastname.pack(pady=5)
    frameRegister.configure(background="#343a40")
    lblLastname = Label(frameLastname, text="Last name: ", fg="white", bg="#343a40", font=("Arial", "10"))
    lblLastname.pack(side=LEFT)
    txtLastname = Entry(frameLastname, font=("Arial", "10"))
    txtLastname.pack()

    frameUsername = Frame(frameRegister)
    frameUsername.pack(pady=5)
    frameRegister.configure(background="#343a40")
    lblUsername = Label(frameUsername, text="Username: ", fg="white",bg="#343a40", font=("Arial", "10"))
    lblUsername.pack(side=LEFT)
    txtUsername = Entry(frameUsername, font=("Arial", "10"))
    txtUsername.pack()

    framePassword = Frame(frameRegister)
    framePassword.pack(pady=5)
    frameRegister.configure(background="#343a40")
    lblPassword = Label(framePassword, text="Password: ", fg="white",bg="#343a40", font=("Arial", "10"))
    lblPassword.pack(side=LEFT)
    txtPassword = Entry(framePassword, show="•", font=("Arial", "10"))
    txtPassword.pack()

    #Dugme za slanje podataka o korisniku pri registraciji
    btnRegisterSubmit = Button(frameRegister, text="REGISTER", command=lambda: RegisterSubmit(txtFirstname.get(),txtLastname.get(),
                                                                                              txtUsername.get(),txtPassword.get()), width=12)
    btnRegisterSubmit.pack(anchor=W, pady=15)

    #Dugme za povratak na pocetnu formu aplikacije
    btnBackToStart = Button(frameRegister, text="START FROM", command=lambda: RegisterToStart(root),width=12)
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

#Funkcija za otvaranje korisnicke forme
def FormUser():
    root = tkinter.Tk()
    root.title("User Form")
    root.configure(background="#343a40")
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - 310
    y = (heightScreen / 2) - 310
    root.geometry('%dx%d+%d+%d' % (620, 620, x, y))

    #Dohvatanje podataka o prijavljenom klijentu
    user = ClientManager.ClientGetData(LOGIN_USER_USERNAME)

    lblUsername = Label(root, text="USER: " + user.firstname + " " + user.lastname, font=("Times", "15"),bg="#343a40",fg="#1a8cff")
    lblUsername.pack(anchor=W, pady=10, padx=20)

    #Dugme za odjavljivanje iz aplikacije i povratak na pocetnu formu
    btnLogout = Button(root,text="LOGOUT", command=lambda: LogoutUser(root),width=12)
    btnLogout.pack(anchor=W, padx=20)

    frameUsers = Frame(root)
    frameUsers.pack(pady=10,padx=20, fill=BOTH)
    frameUsers.configure(background="#343a40")

    frameOnlineUsers = Frame(frameUsers)
    frameOnlineUsers.pack(anchor=W, side=LEFT)
    frameOnlineUsers.configure(background="#343a40")
    lblOnlineUsers = Label(frameOnlineUsers, text="Online users:", font=("Arial", "11"), fg="#28a745", bg="#343a40")
    lblOnlineUsers.pack(anchor=W)

    lbOnlineUsers = Listbox(frameOnlineUsers, selectmode=SINGLE, width=35,height=7,bg="#f8f9fa",font=("Arial", "10"))
    lbOnlineUsers.pack(side=LEFT)
    scrollbarOnline = Scrollbar(frameOnlineUsers, orient="vertical", command=lbOnlineUsers.yview)
    scrollbarOnline.pack(side="right", fill="y")
    lbOnlineUsers.config(yscrollcommand=scrollbarOnline.set)

    frameAllUsers = Frame(frameUsers)
    frameAllUsers.pack(anchor=E)
    frameAllUsers.configure(background="#343a40")
    lblAllUsers = Label(frameAllUsers, text="All users:",font=("Arial", "11"), fg="#dc3545", bg="#343a40")
    lblAllUsers.pack(anchor=W)

    lbAllUsers = Listbox(frameAllUsers, selectmode=SINGLE, width=35, height=7,bg="#f8f9fa",font=("Arial", "10"))
    lbAllUsers.pack(side=LEFT)
    ClientManager.GetAllUsers(LOGIN_USER_USERNAME,lbAllUsers)
    scrollbarAll = Scrollbar(frameAllUsers, orient="vertical", command=lbAllUsers.yview)
    scrollbarAll.pack(side="right", fill="y")
    lbAllUsers.config(yscrollcommand=scrollbarAll.set)

    frameChat = Frame(root)
    frameChat.pack(pady=10)
    frameChat.configure(background="#343a40")

    lblMessages = Label(frameChat,text="Messages:", font=("Arial", "11"),bg="#343a40",fg="white")
    lblMessages.pack(anchor=W)

    frameMessages = Frame(frameChat)
    frameMessages.pack()
    frameMessages.configure(background="#343a40")

    lbMessages = Listbox(frameMessages, selectmode=SINGLE, width=50, height=17,bg="#f8f9fa",font=("Arial", "10"))
    lbMessages.pack(side=LEFT)
    scrollbarMessages = Scrollbar(frameMessages, orient="vertical", command=lbMessages.yview)
    scrollbarMessages.pack(side="right", fill="y")
    lbMessages.config(yscrollcommand=scrollbarMessages.set)
    ClientManager.GetAllMessages(lbMessages)

    frameSendMessage = Frame(frameChat)
    frameSendMessage.pack(fill=BOTH)
    frameSendMessage.configure(background="#343a40")
    txtMessage = Entry(frameSendMessage, width=47,font=("Arial", "10"),bg="#f8f9fa")
    txtMessage.pack(side=LEFT,ipady=3)

    #Dugme za slanje poruke
    btnSendMessage = Button(frameSendMessage,text="send", command=lambda: SendMessage(LOGIN_USER_USERNAME,txtMessage),font=("Arial", "10"))
    btnSendMessage.pack(ipady=1,padx=0)

    #Pokretanje niti koja prati stanje novih poruka i trenutno prijavljenih korisnika
    threading.Thread(target=ClientManager.GetOnlineClientMessages,args=(lbOnlineUsers,lbMessages)).start()

    #Vezivanje funkcije za odjavljivanje
    root.protocol("WM_DELETE_WINDOW", lambda: FormUserClosing(root))
    root.mainloop()

#Funkcija za slanje nove poruke
def SendMessage(username,txtMessage):
    if txtMessage.get() == '':
        messagebox.showinfo("Poruka", "Niste uneli poruku za slanje!")
    else:
        #Prosledjivanje statickoj metodi koja vrsi obradu slanja na server
        ClientManager.SendMessageForAll(username,txtMessage.get())
        txtMessage.delete(0, END)
        txtMessage.insert(0, '')

#Obrada funkcije odjavljivanja prilikom gasenja korisnicke forme
def FormUserClosing(root):
    if messagebox.askokcancel("Odjava", "Da li ste sigurni da zelite da se odjavite?"):
        LogoutUser(root)

#Funkcija za odjavljivanje korisnika
def LogoutUser(root):
    if ClientManager.ClientLogout(LOGIN_USER_USERNAME):
        root.destroy()
        FormStart()


FormStart()


