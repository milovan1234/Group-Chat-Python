# import tkinter as tk
#
# root=tk.Tk()
# f1 = tk.Frame(width=200, height=200, background="red")
# f2 = tk.Frame(width=100, height=100, background="blue")
#
# f1.pack(fill="both", expand=True, padx=20, pady=20)
# f2.place(in_=f1, anchor="c", relx=.5, rely=.5)
#
# root.mainloop()





#klasa za prikaz forme za logovanje
# class FormLogin():
#     def __init__(self):
#         self.root = tkinter.Tk()
#     def Load(self):
#         self.root.title("Login Form")
#         #centriranje forme na sredini ekrana
#         widthScreen = self.root.winfo_screenwidth()
#         heightScreen = self.root.winfo_screenheight()
#         x = (widthScreen / 2) - 150
#         y = (heightScreen / 2) - 150
#         self.root.geometry('%dx%d+%d+%d' % (300, 300, x, y))
#
#         frameLogin = Frame(self.root)
#         frameLogin.place(in_=self.root, anchor="c", relx=0.5, rely=0.5)
#
#         lblLoginTitle = Label(frameLogin,text="Login",font=("Times","15"))
#         lblLoginTitle.pack(pady=15)
#
#         frameUsername = Frame(frameLogin)
#         frameUsername.pack(pady=5)
#         lblUsername = Label(frameUsername,text="Username: ")
#         lblUsername.pack(side=LEFT)
#         txtUsername = Entry(frameUsername)
#         txtUsername.pack()
#
#         framePassword = Frame(frameLogin)
#         framePassword.pack(pady=5)
#         lblPassword = Label(framePassword,text="Password: ")
#         lblPassword.pack(side=LEFT)
#         txtUsername = Entry(framePassword, show="•")
#         txtUsername.pack()
#
#         btnLoginSubmit = Button(frameLogin,text="LOGIN")
#         btnLoginSubmit.pack(anchor=W,pady=10)
#
#         btnBackToStart = Button(frameLogin,text="START FROM",command=lambda: self.OpenStart())
#         btnBackToStart.pack(anchor=W)
#         self.root.mainloop()
#     def OpenStart(self):
#         formStart = FormStart()
#         self.Close()
#         formStart.Load()
#     def Close(self):
#         self.root.destroy()


#klasa za prikaz forme za registraciju
# class FormRegister():
#     def __init__(self):
#         self.root = tkinter.Tk()
#     def Load(self):
#         self.root.title("Register Form")
#         widthScreen = self.root.winfo_screenwidth()
#         heightScreen = self.root.winfo_screenheight()
#         x = (widthScreen / 2) - 150
#         y = (heightScreen / 2) - 150
#         self.root.geometry('%dx%d+%d+%d' % (300, 300, x, y))
#
#         frameRegister = Frame(self.root)
#         frameRegister.place(in_=self.root, anchor="c", relx=0.5, rely=0.5)
#
#         lblRegisterTitle = Label(frameRegister, text="Register", font=("Times", "15"))
#         lblRegisterTitle.pack(pady=15)
#
#         frameFirstname = Frame(frameRegister)
#         frameFirstname.pack(pady=5)
#         lblFirstname = Label(frameFirstname, text="First name: ")
#         lblFirstname.pack(side=LEFT)
#         txtFirstname = Entry(frameFirstname)
#         txtFirstname.pack()
#
#         frameLastname = Frame(frameRegister)
#         frameLastname.pack(pady=5)
#         lblLastname = Label(frameLastname, text="Last name: ")
#         lblLastname.pack(side=LEFT)
#         txtLastname = Entry(frameLastname)
#         txtLastname.pack()
#
#         frameUsername = Frame(frameRegister)
#         frameUsername.pack(pady=5)
#         lblUsername = Label(frameUsername, text="Username: ")
#         lblUsername.pack(side=LEFT)
#         txtUsername = Entry(frameUsername)
#         txtUsername.pack()
#
#         framePassword = Frame(frameRegister)
#         framePassword.pack(pady=5)
#         lblPassword = Label(framePassword, text="Password: ")
#         lblPassword.pack(side=LEFT)
#         txtPassword = Entry(framePassword, show="•")
#         txtPassword.pack()
#
#         btnRegisterSubmit = Button(frameRegister, text="REGISTER")
#         btnRegisterSubmit.pack(anchor=W,pady=10)
#
#         btnBackToStart = Button(frameRegister,text="START FROM",command=lambda: self.OpenStart())
#         btnBackToStart.pack(anchor=W)
#
#         self.root.mainloop()
#     def OpenStart(self):
#         formStart = FormStart()
#         self.Close()
#         formStart.Load()
#     def Close(self):
#         self.root.destroy()






#klasa za prikaz pocetne forme
# class FormStart:
#     def __init__(self):
#         self.root = tkinter.Tk()
#     def Load(self):
#         self.root.title("Start Form")
#         widthScreen = self.root.winfo_screenwidth()
#         heightScreen = self.root.winfo_screenheight()
#         x = (widthScreen/2)-150
#         y = (heightScreen/2)-150
#         self.root.geometry('%dx%d+%d+%d' % (300, 300, x, y))
#
#         frameLogReg = Frame(self.root)
#         frameLogReg.place(in_=self.root, anchor="c", relx=0.5, rely=0.5)
#
#         lblTitle = Label(frameLogReg,text="Group Chat Application",font=("Times","17"))
#         lblTitle.pack(pady=20)
#
#         #dugme za otvaranje login forme
#         btnOpenLogin = Button(frameLogReg,text="LOGIN",command=lambda: self.OpenLogin())
#         btnOpenLogin.pack(pady=5)
#
#         #dugme za otvaranje register forme
#         btnOpenRegister = Button(frameLogReg,text="REGISTER",command=lambda: self.OpenRegister())
#         btnOpenRegister.pack(pady=5)
#
#         self.root.mainloop()
#     def OpenLogin(self):
#         self.Close()
#         FormLogin()
#     def OpenRegister(self):
#         registerForm = FormRegister()
#         self.Close()
#         registerForm.Load()
#     def Close(self):
#         self.root.destroy()

# from functools import reduce
#
# test_list = list(('I', 'L', 'O', 'V', 'E', 'G', 'F', 'G'))
# print(test_list)
# test_list = [reduce(lambda i, j: i + ":" + j, test_list[0 : 4])]
# print(test_list)



# from tkinter import *
#
# root = Tk()
# root.geometry('500x300')
#
# frame = Frame(root)
# frame.place(x = 5, y = 5) # Position of where you would place your listbox
#
# lb = Listbox(frame, width=70, height=6)
# lb.pack(side = 'left',fill = 'y' )
#
# scrollbar = Scrollbar(frame, orient="vertical",command=lb.yview)
# scrollbar.pack(side="right", fill="y")
#
# lb.config(yscrollcommand=scrollbar.set)
#
# for i in range(10):
#     lb.insert(END, 'test'+str(i))
#
# root.mainloop()




