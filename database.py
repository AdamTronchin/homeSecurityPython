from threading import Thread
import mysql.connector

class DatabaseBackend(Thread):
 def initDatabase():
    return 1

 def updateValue(self,name, value):
    print(name)
    print(value)
    
 def readValue():
    return 1