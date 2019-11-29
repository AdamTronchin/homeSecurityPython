from threading import Thread
import mysql.connector

class DatabaseBackend(Thread):
 def updateValue(name, value):
    print(name)
    print(value)
    
 def readValue():
    return 1