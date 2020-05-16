import time
import socket
import threading
from models import WorkDatabase
import os


clients = {}
workDB = WorkDatabase()

def RequestHandling(conn,data):
    global clients
    global db
    request,data = data.split(":-:")
    if request == "LOGIN":
        username,password = data.split(":")
        if not os.path.exists("logs/login_log.txt"):
            file=open("logs/login_log.txt","w")
            file.flush()
            file.close()
        db = workDB.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User'
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            if username in clients.keys():
                file = open("logs/login_log.txt", "a")
                file.write("Username: " + username + ":-:Date and time: " + str(time.ctime(time.time())) + ":-:Response: User already connect\n")
                file.flush()
                file.close()
                conn.send(str.encode("LOGIN:-:EXIST"))
            elif list(filter(lambda x: x[3] == username and x[4] == password, result)).__len__() == 1:
                clients[username] = conn
                file = open("logs/login_log.txt", "a")
                file.write("Username: " + username + ":-:Date and time: " + str(time.ctime(time.time())) + ":-:Response: Success connect\n")
                file.flush()
                file.close()
                conn.send(str.encode("LOGIN:-:SUCCESS"))
            else:
                file = open("logs/login_log.txt", "a")
                file.write("Username: " + username + ":-:Date and time: " + str(time.ctime(time.time())) + ":-:Response: Error connect\n")
                file.flush()
                file.close()
                conn.send(str.encode("LOGIN:-:ERROR"))
                conn.close()
        except:
            print("Error: unable to fecth data")
        db.close()
    elif request == "REGISTER":
        firstname,lastname,username,password = data.split(":")
        db = workDB.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User WHERE username="' + username + '"';
        try:
            cursor.execute(query)
            result = cursor.fetchall()
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
        del clients[username]
        conn.send(str.encode("LOGOUT:-:SUCCESS"))
        conn.close()
    elif request == "GETDATA":
        username = data
        db = workDB.Connect()
        cursor = db.cursor()
        query = 'SELECT * FROM User WHERE username="' + username + '"'
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            print(result[2])
            conn.send(str.encode("GETDATA:-:" + str(result[0]) + ":" + result[1] + ":" + result[2] + ":" +
                                 result[3] + ":" + result[4]))
        except:
            print("Error: unable to fecth data")
        db.close()
    print(clients.__len__())
    print(clients)


HOST=''
PORT=1111
sock = socket.socket()
sock.bind((HOST,PORT))
sock.listen(5)
print("Server running...")
while True:
    conn,addr = sock.accept()
    data = conn.recv(8096).decode()
    threading.Thread(target=RequestHandling,args=(conn,data)).start()
