

# very simple test
# test reading MCP3008 on channel 3
# change channel # in line adc = 0-7
# comnent out channels not in use to focus on channel to focus on

import spidev
import time
from gpiozero import MCP3008

adc0  = MCP3008(channel=0)
adc1 = MCP3008(channel=1)
adc2 = MCP3008(channel=2)
adc3 = MCP3008(channel=3)
adc4 = MCP3008(channel=4)
adc5 = MCP3008(channel=5)
adc6 = MCP3008(channel=6)
adc7 = MCP3008(channel=7)



delay =  .1
spi = spidev.SpiDev()
spi.open(0,0)

while True:
         print ('-----------')
         print(adc0.value)
         print(adc1.value)
         print(adc2.value)
         print(adc3.value)
         print(adc4.value)
         print(adc5.value)
         print(adc6.value)
         print(adc7.value)
         print ('-----------')
         time.sleep(.7)
