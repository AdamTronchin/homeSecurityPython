import smbus
import time
import RPi.GPIO as GPIO
#import adafruit_dht
from database import DatabaseBackend

GPIO.setmode(GPIO.BCM)

#Setup SQL Connection

#Sensor Variables
sensorNames = ["frontDoor", "livingRoomDoor", "backDoor", "garageDoor"]
sensorValues = [0, 0, 0, 0]
sensorValues2 = [0, 0, 0, 0]
sensorPorts = [17, 23, 24, 25]

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

#Setup functions
def reportChanges(val):
  d.updateValue(val)

def reportPanel(value):#Write data to panel
    bus.write_byte(panel2, value)
    bus.write_byte(panel1, value)

def sensorChanges(val1, val2):#compare new sensor values to the last recorded sensor values
  for i in range(0, len(sensorNames)):
    if val1 != val2:
      reportChanges(val2)#call method to update database


skip = 0 # if we should read the sensors or check for changes

def readSensors():
  for x in range(0, len(sensorNames)):
    if skip == 0: #check where to store the sensor data
      sensorValues[x] = GPIO.input(sensorPorts[x])
      skip = 1 #change skip value
    else:
      sensorValues2[x] = GPIO.input(sensorPorts[x])
      skip = 0 #change skip value
  sensorChanges(sensorValues, sensorValues2)

while 1==1:
  readSensors()
