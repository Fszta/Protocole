# coding: utf-8
__author__ = 'Ferszterowski Antoine, antoinefer@hotmail.com'

import time
import sys
import os
import csv
import argparse
from threading import Thread
import RPi.GPIO as GPIO
from ppg_sensor import PulseSensor
from gsr_sensor import GsrSensor

class PhysiologicSignal():

    """Capture des signaux phyisiologiques

    Récupère les valeurs issus de deux capteurs contact:

    capteur 1 : pulse sensor, capteur photopléthysmographique
    ---------

    capteur 2 : gsr sensor, capteur de conductimétrie de la peau
    ---------

    """

    def __init__(self):
        self.sensor_started = False
        self.time_init = time.time()
        self.parser = argparse.ArgumentParser()
        self.gsr_sensor = GsrSensor()
        self.pulse_sensor = PulseSensor()
        self.directory_path = "/home/pi/Desktop/capteur_multiples/data/"

    def run(self):
        """Boucle infinie pour capturer les valeurs des capteurs"""
        self.get_argument()
        self.create_directory()
        self.launch_video_record()

        print("numero participant", self.participant_number)

        if self.sensor_started == False:
            self.sensor_started = True
            self.gsr_sensor.start()
            self.pulse_sensor.start()

        while True:

            time.sleep(0.8)
            if time.time() - self.time_init > 385:
                # Force le GPIO à 0
                self.stop_video_record()

                # Arrête le thread du capteur gsr
                self.gsr_sensor.stop_capture()

                # Arrête le thread du capteur ppg
                self.pulse_sensor.stop_capture()

                # Obtient les valeurs du capteur ppg
                self.value_pulse,self.time_pulse,_ = self.pulse_sensor.get_value()

                # Obtient les valeurs du capteur gsr
                self.value_gsr,self.time_gsr,_ = self.gsr_sensor.get_value()

                # Ecriture des données des capteurs dans deux fichiers csv
                self.write_csv()
                sys.exit(0)

    def write_csv(self):
        """Ecris la data dans deux fichiers csv"""
        self.file_csv_pulse = self.participant_directory + "/pulse.csv"
        self.file_csv_gsr = self.participant_directory +  "/gsr.csv"

        # Création et écriture du csv pour le ppg
        with open(self.file_csv_pulse,'wb') as csvfile_pulse:

            writer = csv.writer(csvfile_pulse)
            i = 0
            while i < len(self.value_pulse):
                writer.writerow([self.value_pulse[i], self.time_pulse[i]])
                i  += 1

        # Création et écriture du csv pour le gsr
        with open(self.file_csv_gsr,'wb') as csvfile_gsr:
            writer = csv.writer(csvfile_gsr)
            j = 0
            while j < len(self.value_gsr):
                writer.writerow([self.value_gsr[j], self.time_gsr[j]])
                j += 1

    def get_argument(self):
        """Récupère les arguments passés en ligne de commande"""

        self.parser.add_argument("participant_number",help="identifiant du participant",
                                 type=int)
        args = self.parser.parse_args()
        self.participant_number = str(args.participant_number)

    def create_directory(self):
        """Créer le répertoire associé au numéro du participant"""

        self.participant_directory = self.directory_path+"participant_"+self.participant_number
        if not os.path.exists(self.participant_directory):
            print("Creation du repertoire... ")
            print(self.participant_number)
            os.makedirs(self.participant_directory)
        print("repertoire:",self.participant_directory)

    def launch_video_record(self):
        """Mise à 1 du GPIO 16"""

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.OUT,initial=GPIO.LOW)

        print(GPIO.input(16))
        GPIO.setwarnings(False)
        GPIO.output(16,True)
        print(GPIO.input(16))
        self.start_stroop_test()

    def stop_video_record(self):
        """Mise à 0 du GPIO 16"""
        GPIO.output(16,False)
        GPIO.cleanup()

    def start_stroop_test(self):
        """Lancement du test de stroop"""
        thread_stroop = StroopTest()
        thread_stroop.start()

class StroopTest(Thread):

    """Thread de lancement du test de stroop"""
    def __init__(self):
        Thread.__init__(self)
        self.command = "omxplayer /home/pi/Desktop/final_protocole.mp4"

    def run(self):
        os.system(self.command)

def Programm():
    physiologic_sig = PhysiologicSignal()
    physiologic_sig.run()


if __name__ == '__main__':
    Programm()

