# coding: utf-8
__author__ = 'Ferszterowski Antoine, antoinefer@hotmail.com'

from picamera import PiCamera
from time import sleep


def Programm():
    camera = PiCamera()
    camera.rotation = 180
 
    camera.start_preview()
    
    # Affiche pendant 500 secondes
    sleep(500)

    camera.stop_preview()
    camera.close()
    print("Fin de l'enregistrement")

    
if __name__ == '__main__':
    Programm()    
