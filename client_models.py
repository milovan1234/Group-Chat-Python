import socket
import json

HOST = '127.0.0.1'
PORT = 1111
SOCK_LOGIN = None
SOCK_LISTEN = False


class ClientManager:
    # Staticka metoda za slanje podataka o korisnickom imenu i lozinki pri prijavljivanju
    @staticmethod
    def ClientLogin(username, password):
        global SOCK_LOGIN, SOCK_LISTEN
        SOCK_LOGIN = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCK_LOGIN.connect((HOST, PORT))
        SOCK_LOGIN.send(str.encode("LOGIN:-:" + username + ":" + password))
        data = SOCK_LOGIN.recv(8096).decode()
        request, response = data.split(":-:")
        # Uspesna prijava
        if response == "SUCCESS":
            SOCK_LISTEN = True
            return username
        # Korisnik je vec prijavljen
        elif response == "EXIST":
            SOCK_LOGIN.close()
            return "Exist"
        # Greska pri unosu podataka
        elif response == "ERROR":
            SOCK_LOGIN.close()
            return "Error"

    # Staticka metoda za registraciju novih korisnika
    @staticmethod
    def ClientRegister(firstname, lastname, username, password):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("REGISTER:-:" + firstname + ":" + lastname + ":" + username + ":" + password))
        data = sock.recv(8096).decode()
        request, response = data.split(":-:")
        sock.close()
        # Uspesna registracija
        if response == "SUCCESS":
            return True
        # Korisnicko ime je zauzeto
        else:
            return False

    # Staticka metoda za odjavljivanje korisnika
    @staticmethod
    def ClientLogout(username):
        global SOCK_LOGIN, SOCK_LISTEN
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("LOGOUT:-:" + username))
        data = sock.recv(8096).decode()
        request, response = data.split(":-:")
        sock.close()
        # Uspesna odjava
        if response == "SUCCESS":
            SOCK_LISTEN = False
            return True
        # U slucaju greske pri odjavljivanju
        else:
            return False

    # Staticka metoda pre koje dobavljamo podatke za prijavljenog korisnika
    @staticmethod
    def ClientGetData(username):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("GETDATA:-:" + username))
        data = sock.recv(8096).decode()
        sock.close()
        request, response = data.split(":-:")
        id, firstname, lastname, username, password = response.split(":")
        return User(id, firstname, lastname, username, password)

    # Staticka metoda uz pomoc koje dohvatamo sve korisnike
    @staticmethod
    def GetAllUsers(username, lbAllUsers):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("ALLUSERS:-:" + username))
        data = sock.recv(8096).decode()
        sock.close()
        request, response = data.split(":-:")
        users = list(map(lambda x: x.split(":")[1] + " " + x.split(":")[2] + " - " + x.split(":")[3], response.split(":*:")))
        for user in users:
            lbAllUsers.insert(lbAllUsers.size(), user)

    # Staticka metoda kojom klijent salje poruku svim ostalim klijentima
    @staticmethod
    def SendMessageForAll(username, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("MESSAGEFORALL:-:" + username + ":" + message))
        data = sock.recv(8096).decode()
        sock.close()

    # Staticka metoda uz pomoc koje dohvatamo sve korisnike koji su trenutno prijavljeni
    @staticmethod
    def GetOnlineClientMessages(lbOnlineUsers, lbMessages):
        while SOCK_LISTEN:
            global SOCK_LOGIN
            data = SOCK_LOGIN.recv(8096).decode()
            if data != '':
                request, response = data.split(":-:")
                if request == "ONLINE":
                    if response != '':
                        users = list(map(lambda x: x.split(":")[1] + " " + x.split(":")[2] + " - " + x.split(":")[3], response.split(":*:")))
                        for user in users:
                            lbOnlineUsers.insert(lbOnlineUsers.size(), user)
                elif request == "NEWONLINE":
                    id, firstname, lastname, username = response.split(":")
                    lbOnlineUsers.insert(lbOnlineUsers.size(), firstname + " " + lastname + " - " + username)
                elif request == "LOGOUTUSER":
                    id, firstname, lastname, username = response.split(":")
                    for i in range(lbOnlineUsers.size()):
                        if lbOnlineUsers.get(i) == firstname + " " + lastname + " - " + username:
                            lbOnlineUsers.delete(i)
                if request == "MESSAGEFORALL":
                    lbMessages.insert(lbMessages.size(), response)

    # Staticka metoda uz pomoc koje dohvatamo sve poruke kada se korisnik prijavi
    @staticmethod
    def GetAllMessages(lbMessages):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(str.encode("GETALLMESSAGE:-:ALL"))
        data = json.loads(sock.recv(8096).decode())
        for message in data:
            lbMessages.insert(lbMessages.size(),
                              str(message["dateAndTime"]) + " - " + message["firstname"] + " " + message[
                                  "lastname"] + "("
                              + message["username"] + "): " + message["message"])
        sock.close()


class User:
    def __init__(self, id, firstname, lastname, username, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def __str__(self):
        return str(self.id) + ":" + self.firstname + ":" + self.lastname + ":" + self.username + ":" + self.password