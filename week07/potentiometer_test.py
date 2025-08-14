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

def ReadChannel(channel):
    adc = spi.xfer2([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])

    data = ((adc[1] & 15 << 8) + adc[2])

    return data

while True:
    for i in range(8):
        reading = ReadChannel(i)
        duty = reading / 1.27
        pi_pwm.ChangeDutyCycle(duty)
        print("Reading=%d" % (reading))
        
        time.sleep(0.5)




    # 
    # for i in range(8):
    #     print('ADC[{}]: {:.2f}'.format(i, ReadChannel(i)))

    
    
    
