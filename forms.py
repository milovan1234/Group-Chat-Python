import tkinter
from tkinter import *

class FormStart:
    def __init__(self):
        self.root = tkinter.Tk()
    def Load(self):
        self.root.minsize(width=300,height=300)
        btnOpenLogin = Button(self.root,text="OPEN LOGIN",command=lambda: self.OpenLogin())
        btnOpenLogin.pack()
        self.root.mainloop()
    def OpenLogin(self):
        loginForm = FormLogin()
        self.Close()
        loginForm.Load()
    def Close(self):
        self.root.destroy()

class FormLogin():
    def __init__(self):
        self.root = tkinter.Tk()
    def Load(self):
        self.root.minsize(width=300,height=300)
        btnBackToStart = Button(self.root,text="BACK",command=lambda: self.OpenStart())
        btnBackToStart.pack()
        self.root.mainloop()
    def OpenStart(self):
        formStart = FormStart()
        self.Close()
        formStart.Load()
    def Close(self):
        self.root.destroy()