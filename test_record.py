# coding: utf-8
__author__ = 'Ferszterowski Antoine, antoinefer@hotmail.com'

import os
from threading import Thread
import argparse
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

def Programm():
    camera = PiCamera()
    camera.rotation = 180
 
    camera.start_preview()
    sleep(500)

    # Fin de l'enregistrement
    
    
    camera.stop_preview()


    self.camera.close()
    print("Fin de l'enregistrement")

    
    
if __name__ == '__main__':
    Programm()    
