# coding: utf-8
__author__ = 'Ferszterowski Antoine, antoinefer@hotmail.com'


import time
import sys
from threading import Thread
import smbus
import matplotlib.pyplot as plt

class GsrSensor(Thread):
    """Capteur de conductimétrie de la peau

    Référence capteur -  GSR v1.2

    Récupère les valeurs du capteur GSR de l'arduino
    en utilisant le protocole I2C.
    L'arduino envoie 2 bytes, dans le cas où la valeur est
    supèrieur à 255 le premier byte est mis à 1 et le deuxième
    commence à se remplir.

    """

    def __init__(self):
        Thread.__init__(self)
        self.address = 0x12
        self.value_sensor = []
        self.time_sensor = []
        self.time_init = time.time()
        self.f_sampling  = 10
        self.stopped = False

    def run(self):
        """Capture les valeurs du capteur à la fréquence f_sampling"""

        revision = ([l[12:-1] for l in open('/proc/cpuinfo','r').readlines() if l[:8]=="Revision"]+['0000'])[0]
        bus = smbus.SMBus(1 if int(revision, 16) >= 4 else 0)

        while not self.stopped:

            time.sleep(1./self.f_sampling)
            bytes = bus.read_i2c_block_data(self.address,0x00,2)

            if bytes[0] == 1:
                value = 255 + bytes[1]
            else:
                value = bytes[1]

            time_value = time.time() - self.time_init
            self.value_sensor.append(value)
            self.time_sensor.append(time_value)

    def get_value(self):
        return self.value_sensor, self.time_sensor,self.f_sampling

    def stop_capture(self):
        self.stopped = True

#def Programm():
#    sensor = GsrSensor()
#    sensor.start()
#    sensor.join()

#if __name__ == '__main__':
#    Programm()




