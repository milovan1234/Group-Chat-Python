import time
import datetime
import socket
import threading
from server_models import *
from functools import reduce
import json

clients = {}


# funkcija za obradu zahteva na serveru
def RequestHandling(conn, data):
    global clients
    request, data = data.split(":-:")
    if request == "LOGIN":
        username, password = data.split(":")
        db = WorkDatabase.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User'
        try:
            cursor.execute(query)
            result = list(map(list, cursor.fetchall()))
        except:
            print("Error: unable to fecth data")
        db.close()
        if username in clients.keys():
            WorkWithFile.WriteAppend("logs/login_log.txt", "Username: " + username + ":-:Date and time: " +
                                     str(time.ctime(time.time())) + ":-:Response: User already connect\n")
            conn.send(str.encode("LOGIN:-:EXIST"))
            conn.close()
        elif list(filter(lambda x: x[3] == username and x[4] == password, result)).__len__() == 1:
            clients[username] = conn
            WorkWithFile.WriteAppend("logs/login_log.txt", "Username: " + username + ":-:Date and time: " + str(
                time.ctime(time.time())) + ":-:Response: Success connect\n")
            onlineUsers = ''
            newonline = ''
            for res in result:
                if res[3] in clients.keys() and res[3] != username:
                    onlineUsers += reduce(lambda i, j: str(i) + ":" + str(j), res[0: 4]) + ":*:"
                if res[3] == username:
                    newonline = reduce(lambda i, j: str(i) + ":" + str(j), res[0: 4])
            conn.send(str.encode("LOGIN:-:SUCCESS"))
            clients[username].send(str.encode("ONLINE:-:" + onlineUsers[0:onlineUsers.__len__() - 3]))
            for key in clients:
                if key != username:
                    clients[key].send(str.encode("NEWONLINE:-:" + newonline))
        else:
            WorkWithFile.WriteAppend("logs/login_log.txt", "Username: " + username + ":-:Date and time: " + str(
                time.ctime(time.time())) + ":-:Response: Error connect\n")
            conn.send(str.encode("LOGIN:-:ERROR"))
            conn.close()
    elif request == "REGISTER":
        firstname, lastname, username, password = data.split(":")
        db = WorkDatabase.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User WHERE username="' + username + '"'
        try:
            cursor.execute(query)
            result = map(list, cursor.fetchall())
            if result.__len__() == 1:
                conn.send(str.encode("REGISTER:-:ERROR"))
            else:
                query = 'INSERT INTO User(Firstname,Lastname,Username,Password)' \
                        'VALUES("' + firstname + '", "' + lastname + '", "' + username + '","' + password + '")'
                cursor.execute(query)
                db.commit()
                conn.send(str.encode("REGISTER:-:SUCCESS"))
        except:
            print("Error: unable to fecth data")
        conn.close()
    elif request == "LOGOUT":
        username = data
        db = WorkDatabase.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User WHERE username="' + username + '"'
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            logoutuser = reduce(lambda i, j: str(i) + ":" + str(j), result[0: 4])
        except:
            print("Error: unable to fecth data")
        db.close()
        del clients[username]
        for key in clients:
            clients[key].send(str.encode("LOGOUTUSER:-:" + logoutuser))
        conn.send(str.encode("LOGOUT:-:SUCCESS"))
        conn.close()
    elif request == "GETDATA":
        username = data
        db = WorkDatabase.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User WHERE username="' + username + '"'
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            resultReduce = reduce(lambda i, j: str(i) + ":" + str(j), result[0: 5])
            conn.send(str.encode("GETDATA:-:" + resultReduce))
        except:
            print("Error: unable to fecth data")
        db.close()
        conn.close()
    elif request == "ALLUSERS":
        username = data
        db = WorkDatabase.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User WHERE username!="' + username + '"'
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            allusers = ''
            for res in result:
                allusers += reduce(lambda i, j: str(i) + ":" + str(j), res[0: 4]) + ":*:"
            conn.send(str.encode("ALLUSERS:-:" + allusers[0:allusers.__len__() - 3]))
        except:
            print("Error: unable to fecth data")
        db.close()
        conn.close()
    elif request == "MESSAGEFORALL":
        username, message = data.split(":")
        db = WorkDatabase.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User WHERE username="' + username + '"'
        try:
            cursor.execute(query)
            result = cursor.fetchone()
        except:
            print("Error: unable to fecth data")
        db.close()
        WorkWithJson.WriteNew('json/messages.json', Message(result[1], result[2], result[3],
                                                            datetime.datetime.now().strftime('%d.%m.%Y. %H:%M'),
                                                            message))
        for key in clients:
            clients[key].send(str.encode("MESSAGEFORALL:-:" + str(datetime.datetime.now().strftime('%d.%m.%Y. %H:%M')) + " - " +
                                                            result[1] + " " + result[2] + "(" + result[3] + "): " + message))
        conn.send(str.encode("SUCCESS"))
        conn.close()
    elif request == "GETALLMESSAGE":
        response = WorkWithJson.ReadAll('json/messages.json')
        conn.send(str.encode(json.dumps(response)))
        conn.close()

    print(clients.__len__())
    print(clients)


HOST = ''
PORT = 1111
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(5)
print("Server running...")
while True:
    conn, addr = sock.accept()
    data = conn.recv(8096).decode()
    threading.Thread(target=RequestHandling, args=(conn, data)).start()