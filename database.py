from threading import Thread
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.2.54",
  user="pi",
  passwd="PASSpass9",
  database="homeSecurity"
)

class DatabaseBackend(Thread):
 def initDatabase():
    mycursor = mydb.cursor()


 def updateValue(self,name, value):
    print(name)
    print(value)
    
 def readValue(self):
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)