import RPi.GPIO as GPIO

def check_gpio():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(GPIO.input(12))

check_gpio()

