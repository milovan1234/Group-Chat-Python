import socket
import pymysql
import threading

HOST='127.0.0.1'
PORT=1111
global SOCK_LOGIN


class ClientManager:
    @staticmethod
    def ClientLogin(username,password):
        global SOCK_LOGIN
        SOCK_LOGIN = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCK_LOGIN.connect((HOST, PORT))
        SOCK_LOGIN.send(str.encode("LOGIN:-:" + username + ":" + password))
        data = SOCK_LOGIN.recv(8096).decode()
        request,response = data.split(":-:")
        if response == "SUCCESS":
            return username,SOCK_LOGIN
        elif response == "EXIST":
            return "Exist",""
        else:
            return "Error",""
            sockLogin.close()
    @staticmethod
    def ClientRegister(firstname,lastname,username,password):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("REGISTER:-:"+ firstname + ":" + lastname + ":" + username + ":" + password))
        data = sock.recv(8096).decode()
        request, response = data.split(":-:")
        if response == "SUCCESS":
            return True
        else:
            return False
        sock.close()
    @staticmethod
    def ClientLogout(username):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("LOGOUT:-:" + username))
        data = sock.recv(8096).decode()
        request, response = data.split(":-:")
        if response == "SUCCESS":
            return True
            sockLogin.close()
        else:
            return False
        sock.close()
    @staticmethod
    def ClientGetData(username):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("GETDATA:-:" + username))
        data = sock.recv(8096).decode()
        request, response = data.split(":-:")
        id,firstname,lastname,username,password=response.split(":")
        return User(id,firstname,lastname,username,password)

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


