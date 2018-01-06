#!/usr/bin/env python2.7

import sys
import time
from subprocess import PIPE, Popen
from low_battery_en import * #Import the graphic code.

criticalBat = 10 #Configure the critical level of the battery.

class lowBaterry(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

def mostrar(): #Shows the notification of the battery low.
    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = lowBaterry()
        myapp.show()
        sys.exit(app.exec_())

def estado(salida): #Check that the charger is plugged-in.
    if salida[11] == 'C':
        x = 1 #The charger is plugged-in.
    else:
        x = 0 #The charger is not plugged-in.
    return x

def porcentaje(salida): #Gets the percentage of the battery.
    try:
        if estado(salida) == 1:
            porcentaje = int(salida[21] + salida[22])
        else:
            porcentaje = int(salida[24] + salida[25])
        return porcentaje

    except:
            if estado(salida) == 1:
                porcentaje = int(salida[23] + salida[24])
            else:
                porcentaje = int(salida[26] + salida[27])
            return porcentaje
def verificar(salida, minBat):
    if porcentaje(salida) <= minBat and estado(salida) == 0:
        mostrar()

def tiempo(salida, minBat):
    bat = porcentaje(salida)
    if bat <= minBat + 10:
        time = 60 #1 minute to do again the verificacion if the level battery is low.
    else:
        time = 500 #5 minutes to do again the verificacion if the level battery is high.
    return time

while True:
    mostrar()
    lectura = Popen(['acpi'], stdout=PIPE, stderr=PIPE) #Runs the command acpi.
    salida = str(lectura.stdout.read()) #Stores the output of the command acpi.
    verificar(salida, criticalBat) #Checks the state of the battery.
    time.sleep(tiempo(salida, criticalBat)) #Sets the time to do the cheking.
