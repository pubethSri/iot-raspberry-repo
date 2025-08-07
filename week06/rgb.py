import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
RED = 5
BLUE = 6
GREEN = 13

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

def shut():
    GPIO.output(RED, True)
    GPIO.output(BLUE, True)
    GPIO.output(GREEN, True)

while True:
    GPIO.output(RED, False)
    GPIO.output(BLUE, True)
    GPIO.output(GREEN, True)
    time.sleep(0.5)
    shut()
    time.sleep(0.5)

    GPIO.output(RED, True)
    GPIO.output(BLUE, False)
    GPIO.output(GREEN, True)
    time.sleep(0.5)
    shut()
    time.sleep(0.5)

    GPIO.output(RED, True)
    GPIO.output(BLUE, True)
    GPIO.output(GREEN, False)
    time.sleep(0.5)
    shut()
    time.sleep(0.5)

    GPIO.output(RED, False)
    GPIO.output(BLUE, False)
    GPIO.output(GREEN, True)
    time.sleep(0.5)
    shut()
    time.sleep(0.5)

    GPIO.output(RED, False)
    GPIO.output(BLUE, True)
    GPIO.output(GREEN, False)
    time.sleep(0.5)
    shut()
    time.sleep(0.5)

    GPIO.output(RED, True)
    GPIO.output(BLUE, False)
    GPIO.output(GREEN, False)
    time.sleep(0.5)
    shut()
    time.sleep(0.5)

    GPIO.output(RED, False)
    GPIO.output(BLUE, False)
    GPIO.output(GREEN, False)
    time.sleep(0.5)
    shut()
    time.sleep(0.5)
