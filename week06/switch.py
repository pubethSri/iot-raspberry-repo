import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LIGHT = 4

GPIO.setup(LIGHT, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

val = GPIO.input(17)

while True:
    prin(val)