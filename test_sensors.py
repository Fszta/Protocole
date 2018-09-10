# coding: utf-8
__author__='Ferszterowski Antoine, antoinefer@hotmail.com'

import time
from  ppg_sensor import PulseSensor
from gsr_sensor import GsrSensor
import matplotlib.pyplot as plt


def Programm():
    test_sensor = TestSensor()
    test_sensor.run()


class TestSensor():
    """ Code pour tester le bon positionnement du capteur sur le doigt"""

    def __init__(self):
        self.pulse_sensor = PulseSensor()
        self.gsr_sensor = GsrSensor()
        self.time_init = time.time()

    def run(self):
        """Récupère les valeurs du capteur après 15 secondes"""

        print("Debut capture...")
        self.pulse_sensor.start()
        self.gsr_sensor.start()

        while True:
            time.sleep(1)
            if time.time() - self.time_init > 15:
                self.pulse_sensor.stop_capture()
                self.gsr_sensor.stop_capture()

                self.value_pulse, self.time_pulse, _ = self.pulse_sensor.get_value()
                self.value_gsr, self.time_gsr, _= self.gsr_sensor.get_value()

                print("Fin capture...")
                plt.plot(self.time_pulse,self.value_pulse)
                plt.show()
                plt.plot(self.time_gsr, self.value_gsr)
                plt.show()
                break

if __name__ == '__main__':
    Programm()
