import time
import spidev
import math

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000

def ReadChannel(channel):
    adc = spi.xfer2([6 | (channel >> 2), (channel & 3) << 6, 0])
    data = ((adc[1] & 0x0F) << 8) | adc[2]
    return data

# --- Thermistor (TTC05103) ---
Vref = 3.3
R_fixed = 10000  # 10k resistor in divider
T0 = 298.15      # 25°C in Kelvin
R0 = 10000       # 10k at 25°C
Beta = 3950      # from datasheet

def read_thermistor(channel):
    adc_val = ReadChannel(channel)
    Vout = adc_val * Vref / 4095
    # voltage divider: Vout = Vref * (R_therm / (R_fixed + R_therm))
    R_therm = R_fixed * Vout / (Vref - Vout)

    # Beta equation:
    tempK = 1 / (1/T0 + (1/Beta) * math.log(R_therm / R0))
    tempC = tempK - 273.15
    return tempC

--- MCP9700 ---
def read_mcp9700(channel):
    adc_val = ReadChannel(channel)
    Vout = adc_val * Vref / 4095
    print("Raw Vout = %.3f V" % Vout)
    tempC = (Vout - 0.5) / 0.01
    return tempC


while True:
    # temp_ntc = read_thermistor(0)   # assume thermistor on CH0
    temp_mcp = read_mcp9700(0)      # assume MCP9700 on CH1

    print("MCP9700: %.2f °C" % (temp_mcp))
    # print("Thermistor: %.2f °C\t MCP9700: %.2f °C" % (temp_ntc, temp_mcp))
    time.sleep(1)
