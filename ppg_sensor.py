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
            if len(self.signal_sensor) >  6500:
                self.signal_sensor = self.signal_sensor[len(self.signal_sensor)-6500:]
                self.time = self.time[len(self.time)-6500:]
            signal = self.adc.read(self.channel)
            self.signal_sensor.append(signal)
            self.time.append(time.time() - self.time_start)
            time.sleep(1./200)
            #print(signal)

    def get_value(self):

        fs = int(len(self.signal_sensor)/(time.time() - self.time_start))
        filtered_signal = filtrage.run(self.signal_sensor,self.time_start,fs,0.8,4,4)
        #filtered_signal = self.signal_sensor
        return filtered_signal, self.time, fs


    def reset_signal(self):
        print("Reset signal capteur...")
        self.signal_sensor = []
        self.time = []


    def stop_capture(self):
        self.stopped = True

