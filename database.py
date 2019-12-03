from threading import Thread
import mysql.connector

class DatabaseBackend(Thread):
 def updateValue(self, name, value):
    print(convertToASIC(name))
    print(value)
    
 def readValue(self):
    return 1
 
 def convertToASIC(string):
    for x in string:
       return ord(x)