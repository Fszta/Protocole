# coding: utf-8
__author__ = 'Ferszterowski Antoine, antoinefer@hotmail.com'

import os
from threading import Thread
import argparse
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

def Programm():
    recorder = Record()
    recorder.check_gpio()

class Record():
    """Enregistrement d'une video avec la PiCamera"""

    def __init__(self,duration = 389):
        self.duration_capture = duration
        #self.record_path = "/home/pi/Desktop/video_dataset/record/record_no_"
        self.record_path = "/media/pi/VERBATIM HD/PC/video_dataset/record/record_no_"
        self.codec_video = ".h264"
        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.framerate = 30
        self.camera.resolution = (1920,1080)
        self.parser = argparse.ArgumentParser()
        self.start_record = False

    def get_argument(self):
        """Récupère les arguments passés en lignes de commandes"""

        self.parser.add_argument("participant_number", help ="Nomme le fichier à partir du numéro du participant",
                                 type=int)
        args = self.parser.parse_args()
        self.participant_number = str(args.participant_number)

    def capture(self):

        self.get_argument()
        print("Numero du participant",self.participant_number)
        print("Format d'encodage:",self.codec_video)
        print("Debut de l'enregistrement...")

        #self.camera.start_preview()
        #self.camera.annotate_text = "Record No"  + self.participant_number

        # Enregistrement du flux video
        # Chemin + numéro du participant + extension du fichier
        self.camera.start_recording(self.record_path+self.participant_number+self.codec_video)

        # Durée de la capture
        sleep(self.duration_capture)

        # Fin de l'enregistrement
        self.camera.stop_recording()
        #self.camera.stop_preview()

        # Passe le flag à True, arrête la boucle infinie
        self.record_ended = True
        self.camera.close()
        print("Fin de l'enregistrement")

    def check_gpio(self):
        """ Check l'état du GPIO 12 """

        # Flag utilisé pour la boucle infinie
        self.record_ended = False

        # Mode de sélection des pins
        GPIO.setmode(GPIO.BCM)

        # Initialise à 0
        GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        while not self.record_ended :

            # Test toutes les secondes
            sleep(0.5)
            print("Check GPIO 12...")

            # Si la capture n'a pas commencé et que l'autre pi force le gpio 12 à 1
            if GPIO.input(12) == 1 and self.start_record == False:
                print("Debut enregistrement")
                self.start_record = True
                #thread_stroop = StroopTest()
                #thread_stroop.start()

                self.capture()

class StroopTest(Thread):
    """Thread de lancement du test de stroop"""

    def __init__(self):
        Thread.__init__(self)
        self.command = "omxplayer /home/pi/Desktop/videoProtocole.mp4"
        #self.command = "ls"
    def run(self):
        os.system(self.command)

if __name__ == '__main__':
    Programm()
