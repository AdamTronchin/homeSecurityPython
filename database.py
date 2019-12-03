from threading import Thread
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.2.54",
  user="pi",
  passwd="PASSpass9",
  database="homeSecurity"
)

mycursor = mydb.cursor()

class DatabaseBackend(Thread):
 def updateValue(self, name, value):
    print(convertToASIC(name))
    print(value)
    
 def readValue(self):
    return 1
 
 def convertToASIC(string):
    for x in string:
       return ord(x)
 def initDatabase(self):
    print("Pass") 

 def updateValue(self,name, value):
    print(name)
    print(value)
    
 def readValue(self):
    mycursor.execute("SELECT * FROM doors")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
