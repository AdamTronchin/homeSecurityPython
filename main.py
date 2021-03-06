import smbus
import RPi.GPIO as GPIO
from gpiozero import Button
#import adafruit_dht
from database import DatabaseBackend
import time

GPIO.setmode(GPIO.BCM)

#Setup SQL Connection

#Sensor Variables
sensorNames = ["frontDoor", "backDoor"]
sensorValues = [False,False]
sensorValues2 = [False, False]
sensorPorts = [17,27]
sensorList = []

# other variables
skip = 0 # if we should read the sensors or check for changes

#Panel bus Address variables
panel1 = 0x07
panel2 = 0x08

#Setup I2C on bus 1
bus = smbus.SMBus(1)

#Initialize Database Object
d = DatabaseBackend()

#Set device to input
#bus.write_byte(view2,0xFF)

#Setup GPIO Sensor Pins
for i in sensorPorts:
 GPIO.setup(i,GPIO.IN)#Setup all gpio sensors

for i in sensorPorts:
  sensorList.append(Button(sensorPorts))

#Setup Temp Sensors
#dhtDevice = adafruit_dht.DHT22(board.D18)
 #temperature_c = dhtDevice.temperature
 #       temperature_f = temperature_c * (9 / 5) + 32
 #       humidity = dhtDevice.humidity
  #      print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% "
   #           .format(temperature_f, temperature_c, humidity))

#Setup functions
def reportChanges(pos):
  d.updateValue(sensorNames[pos], sensorValues[pos])
  print(sensorNames[pos]+str(sensorValues[pos]))

def reportPanel(value):#Write data to panel
    bus.write_byte(panel2, value)
    bus.write_byte(panel1, value)

def sensorChanges(val1, val2):#compare new sensor values to the last recorded sensor values
  for i in range(0, len(sensorNames)):
    if val1 != val2:
      reportChanges(i)#call method to update database

#sensorValues[x] = GPIO.input(sensorPorts[x])
def readSensors():
  for x in range(0, len(sensorNames)):
   sensorValues[x] = sensorList[x]
    
#sensorValues2[x] = GPIO.input(sensorPorts[x])
def readSensors2():
  for x in range(0, len(sensorNames)):
   sensorValues2[x] = sensorList[x]

   
      

skip = 0
while 1==1:
  sensorChanges(sensorValues, sensorValues2)
  if(skip == 0):
    skip = 1
    readSensors()
  else:
    skip = 0
    readSensors2()
