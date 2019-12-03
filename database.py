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
   #convertToASIC(name)
   sql = "UPDATE doors SET"+name+"= 'Canyon 123' WHERE address = 'Valley 345'"
   mycursor.execute(sql)
   mydb.commit()
 
 def convertToASIC(self, string):
    for x in len(string):
       return ord(x)

 def initDatabase(self):
    print("Pass") 
    
 def readValue(self):
    mycursor.execute("SELECT * FROM doors")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
