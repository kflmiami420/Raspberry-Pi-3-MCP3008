
#
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print('-----------------------------------')
print('Reading MCP3008 values 4 channels,')
print('Press Ctrl-C to quit...')
print('|  {1:>4} | {2:>4} | {3:>4} | {4:>5} |'.format(*range(5)))
print('-----------------------------------' )

while True:
    values = [0]*5
    for i in range(5):
        values[i] = mcp.read_adc(i)

    print('|  {1:>4} | {2:>4} | {3:>4}|{4:>5}  |'.format(*values))
    time.sleep(0.5)
#------------------------------------------------------
