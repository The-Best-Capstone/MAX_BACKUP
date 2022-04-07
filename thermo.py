import time
import Adafruit_MAX31855.MAX31855 as MAX31855
# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 24
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)


print('Press Ctrl-C to quit.')
while True:
    temp = sensor.readTempC()
    internal = sensor.readInternalC()
    print('Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, (temp* 1.8 + 32)))
    print('    Internal Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal, (internal* 1.8 + 32)))
    time.sleep(1)
