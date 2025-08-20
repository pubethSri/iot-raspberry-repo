import time
import spidev
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
ledpin = 12

GPIO.setup(ledpin, GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin, 1000)
pi_pwm.start(0)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000

def ReadChannel(channel):
    adc = spi.xfer2([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])

    data = ((adc[1] & 15 << 8) + adc[2])

    return data

while True:
    for i in range(8):
        temp = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
        reading = ReadChannel(0)
        voltage = reading * 3.3 / 4096
        forduty = reading / 2.55
        temp[i] = forduty
    print("Reading=%d\t Voltage=%f\t Forduty=%f" %(reading, voltage, min(temp)))
    pi_pwm.ChangeDutyCycle(min(temp))

    time.sleep(0.5)

