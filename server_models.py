import json
import pymysql
import datetime
import os

#Klasa za rad sa bazom
class WorkDatabase:
    #Metoda koja vraca konekciju na pimysql bazu
    @staticmethod
    def Connect():
        return pymysql.connect(host="localhost", port=3306, user="root", password="", db="group-chat")


#Klasa za obradu poruka
class Message:
    def __init__(self,firstname,lastname,username,dateAndTime, message):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.dateAndTime = dateAndTime
        self.message = message
    def to_json(self):
        return json.dumps(self.__dict__)

#Klasa za rad sa JSON fajlom
class WorkWithJson:
    #Staticka metoda za citanje svih podataka iz fajla i vracanje liste objekata
    @staticmethod
    def ReadAll(path):
        if not os.path.exists(path):
            file=open(path,"w")
            file.write('[]')
            file.flush()
            file.close()
        with open(path, 'r') as f:
            return list(json.load(f))
    #Staticka metoda za upis novog objekta u JSON fajl
    @staticmethod
    def WriteNew(path,object):
        if not os.path.exists(path):
            file=open(path,"w")
            file.write('[]')
            file.flush()
            file.close()
        data = WorkWithJson.ReadAll(path)
        data.append(json.loads(object.to_json()))
        with open(path, 'w') as json_file:
            json.dump(data, json_file)

#Klasa za rad sa tekstualnim fajlom
class WorkWithFile:
    #Staticka metoda za upisivanje novog reda u fajl, u mom slucaju sluzi kao log fajl prilikom prijavljvanja
    @staticmethod
    def WriteAppend(path, text):
        if not os.path.exists(path):
            file = open(path, "w")
            file.write(text)
            file.flush()
            file.close()
        else:
            file = open(path, "a")
            file.write(text)
            file.flush()
            file.close()