import RPi.GPIO as GPIO
import time

def rgb(red, green, blue):
    GPIO.output(RED, red)
    GPIO.output(BLUE, green)
    GPIO.output(GREEN, blue)

KEYPAD = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']
]

ROWS = [4, 17, 27, 22]
COLS = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)

RED = 23
BLUE = 24
GREEN = 25

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

for row_pin in ROWS:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for col_pin in COLS:
    GPIO.setup(col_pin, GPIO.OUT)
    GPIO.output(col_pin, GPIO.HIGH)

def get_key():
    key = None

    for col_num, col_pin in enumerate(COLS):
        GPIO.output(col_pin, GPIO.LOW)

        for row_num, row_pin in enumerate(ROWS):
            if GPIO.input(row_pin) == GPIO.LOW:
                key = KEYPAD[row_num] [col_num]

                while GPIO.input(row_pin) == GPIO.LOW:
                    time.sleep(0.05)

        GPIO.output(col_pin, GPIO.HIGH)

    return key

try:
    while True:
        pressed_key = get_key()

        if pressed_key is not None:
            print(f"Pressed: {pressed_key}")
            if (pressed_key == 1):
                rgb(False, True, True)
            elif (pressed_key == 2):
                rgb(True, False, True)
            elif (pressed_key == 3):
                rgb(True, True, False)
            elif (pressed_key == 4):
                rgb(False, False, True)
            elif (pressed_key == 5):
                rgb(False, True, False)
            elif (pressed_key == 6):
                rgb(True, False, False)
            elif (pressed_key == 7):
                rgb(False, False, False)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
