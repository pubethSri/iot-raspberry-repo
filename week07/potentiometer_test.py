import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel):
    adc = spi.xfer2([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])

    data = ((adc[1] & 15 << 8) + adc[2])

    return data

while True:
    # reading = ReadChannel(0)
    # voltage = reading * 3.3 / 4096
    # print("Reading=%d\t Voltage=%f" % (reading, voltage))
    for i in range(8):
        print('ADC[{}]: {:.2f}'.format(i, ReadChannel(i)))
    
    time.sleep(0.2)
