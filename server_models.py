import json
import pymysql
import datetime
import os

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


class Message:
    def __init__(self,firstname,lastname,username,dateAndTime, message):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.dateAndTime = dateAndTime
        self.message = message
    def to_json(self):
        return json.dumps(self.__dict__)


class WorkWithJson:
    @staticmethod
    def ReadAll(path):
        with open(path, 'r') as f:
            return list(json.load(f))
    @staticmethod
    def WriteNew(path,object):
        if not os.path.exists(path):
            file=open(path,"w")
            file.write('[]')
            file.flush()
            file.close()
        with open(path, 'r') as f:
            data = list(json.load(f))
        data.append(json.loads(object.to_json()))
        with open(path, 'w') as json_file:
            json.dump(data, json_file)


class WorkWithFile:
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







