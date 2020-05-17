import socket
import pymysql
import threading

HOST='127.0.0.1'
PORT=1111
SOCK_LOGIN=''
SOCK_LISTEN = False

class ClientManager:
    @staticmethod
    def ClientLogin(username,password):
        global SOCK_LOGIN,SOCK_LISTEN
        SOCK_LOGIN = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCK_LOGIN.connect((HOST, PORT))
        SOCK_LOGIN.send(str.encode("LOGIN:-:" + username + ":" + password))
        data = SOCK_LOGIN.recv(8096).decode()
        request,response = data.split(":-:")
        if response == "SUCCESS":
            SOCK_LISTEN = True
            return username
        elif response == "EXIST":
            SOCK_LOGIN.close()
            return "Exist"
        elif response == "ERROR":
            SOCK_LOGIN.close()
            return "Error"

    @staticmethod
    def ClientRegister(firstname,lastname,username,password):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("REGISTER:-:"+ firstname + ":" + lastname + ":" + username + ":" + password))
        data = sock.recv(8096).decode()
        request, response = data.split(":-:")
        sock.close()
        if response == "SUCCESS":
            return True
        else:
            return False

    @staticmethod
    def ClientLogout(username):
        global SOCK_LOGIN,SOCK_LISTEN
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("LOGOUT:-:" + username))
        data = sock.recv(8096).decode()
        request, response = data.split(":-:")
        sock.close()
        if response == "SUCCESS":
            SOCK_LISTEN = False
            return True
        else:
            return False

    @staticmethod
    def ClientGetData(username):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("GETDATA:-:" + username))
        data = sock.recv(8096).decode()
        sock.close()
        request, response = data.split(":-:")
        id,firstname,lastname,username,password=response.split(":")
        return User(id,firstname,lastname,username,password)

    @staticmethod
    def GetOnlineClient(lbOnlineUsers):
        while SOCK_LISTEN:
            global SOCK_LOGIN
            data = SOCK_LOGIN.recv(8096).decode()
            if data != '':
                request, response = data.split(":-:")
                if request == "ONLINE":
                    if response != '':
                        for user in list(map(lambda x: x.split(":")[1] + " " +
                                                x.split(":")[2] + " - " + x.split(":")[3],response.split(":*:"))):
                            lbOnlineUsers.insert(lbOnlineUsers.size(),user)
                elif request == "NEWONLINE":
                    id,firstname,lastname,username = response.split(":")
                    lbOnlineUsers.insert(lbOnlineUsers.size(),firstname + " " + lastname + " - " + username)
                elif request == "LOGOUTUSER":
                    id,firstname,lastname,username = response.split(":")
                    for i in range(lbOnlineUsers.size()):
                        if lbOnlineUsers.get(i) == firstname + " " + lastname + " - " + username:
                            lbOnlineUsers.delete(i)



class WorkDatabase:
    __instance = None
    @staticmethod
    def getInstance():
        if WorkDatabase.__instance == None:
            WorkDatabase()
        return WorkDatabase.__instance
    def __init__(self):
        if WorkDatabase.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            WorkDatabase.__instance = self
    def Connect(self):
        return pymysql.connect(host="localhost", port=3306, user="root", password="", db="group-chat")



class User:
    def __init__(self, id, firstname,lastname,username,password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
    def __str__(self):
        return str(self.id) + ":" + self.firstname + ":" + self.lastname + ":" + self.username + ":" + self.password


