# coding: utf-8
import time
import sys
from threading import Thread
from MCP3008 import MCP3008
import filtrage

class PulseSensor (Thread):
    """Capteur contact """

    def __init__(self, bus = 0, device = 0, channel = 0):
        Thread.__init__(self)
        self.channel = channel
        self.time_start = time.time()
        self.signal_sensor = []
        self.time = []
        self.adc = MCP3008(bus, device)
        self.stopped = False

    def run(self):
        """Boucle infinie, capture"""
        while not self.stopped :
            
            signal = self.adc.read(self.channel)
            self.signal_sensor.append(signal)
            self.time.append(time.time() - self.time_start)
            time.sleep(1./200)


    def get_value(self):
        """Calcul de f_sampling, filtrage du signal par passe bande"""
        fs = int(len(self.signal_sensor)/(time.time() - self.time_start))
        filtered_signal = filtrage.run(self.signal_sensor,self.time_start,fs,0.7,4,4)

        return filtered_signal, self.time, fs


    def reset_signal(self):
        """Réinitialisation du signal"""
        print("Reset signal capteur...")
        self.signal_sensor = []
        self.time = []


    def stop_capture(self):
        self.stopped = True

