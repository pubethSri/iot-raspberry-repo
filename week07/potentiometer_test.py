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
    reading = ReadChannel(0)
    voltage = reading * 3.3 / 4096
    forduty = reading / 2.55
    print("Reading=%d\t Voltage=%f\t Forduty=%f" %(reading, voltage, forduty))
    pi_pwm.ChangeDutyCycle(forduty) 

    time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
