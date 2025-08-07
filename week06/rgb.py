import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
RED = 5
BLUE = 6
GREEN = 13

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

while True:
    GPIO.output(RED, True)
    GPIO.output(BLUE, False)
    GPIO.output(GREEN, False)
    time.sleep(0.5)
    GPIO.output(RED, False)
    GPIO.output(BLUE, False)
    GPIO.output(GREEN, False)
    time.sleep(0.5)
