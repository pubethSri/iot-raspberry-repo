import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LIGHT = 4

GPIO.setup(LIGHT, GPIO.OUT)
GPIO.setup(17, GPIO.IN)



while True:
    val = GPIO.input(17)
    if val == 1:
        GPIO.output(LIGHT, False)
    else:
        GPIO.output(LIGHT, True)