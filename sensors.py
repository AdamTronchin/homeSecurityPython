from gpiozero import LED, Button
from time import sleep

class Sensors(Button):
    port = 0
    name = ""

    def __init__(self, name, port):
        name = self.name
        port = self.port
        super.__init__(port)

    def createSensors(self,sensorNames,SensorPorts):
        for i in len(sensorNames):
            sensorList.append(Sensors(sensorNames[i],SensorPorts[i]))

    def 