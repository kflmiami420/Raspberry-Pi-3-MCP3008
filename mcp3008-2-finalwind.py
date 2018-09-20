#####
import time
import spidev
from time import sleep

spi = spidev.SpiDev()
spi.open(0,0)

tempChannel    = 1
lightChannel   = 2
windChannel    = 3
direcChannel   = 4

def getReading(channel):
    rawData = spi.xfer([1, (8 + channel) << 4, 0])
    processedData = ((rawData[1]&3) << 8) + rawData[2]
    return processedData

def convertVoltage(bitValue, decimalPlaces=2):
    voltage = (bitValue * 3.3) / float(1023)
    voltage = round(voltage, decimalPlaces)
    return voltage

def convertTemp(bitValue, decimalPlaces=3):
    temperature        = ((bitValue * 330)/float(1023) - 50)
    temp_F             = ((temperature * 9/5) + 32)
    temperature        = round(temperature, decimalPlaces)
    return temp_F

def convertWind(bitValue, decimalPlaces=1):
    windms            = ((bitValue * 3.3) / float(1023) - .00005)
    windms2           = (((windms - 0.4) * 20.25) - .4)
    mph               = ((windms2 * 2.237136)-.5)
    mph               = round(mph, decimalPlaces)
    
    
#    if windms2 <= 1.23:
#            mph = 0
#        else:
#            windms2 = ((windms - 0.4) * 20.25)
    
    return  mph

def convertDirec(bitValue, decimalPlaces=2):
    winddirect        =  299 #Still working on the N/S/E/W  and all the in betwee$
    winddirect        = round(winddirect, decimalPlaces)
    return winddirect

while True:

    lightData      = getReading(lightChannel)
    tempData       = getReading(tempChannel)
    direcData      = getReading(direcChannel)
    windData       = getReading(windChannel)
    speedData      = getReading(windChannel)
    lightVoltage   = convertVoltage(lightData)
    tempVoltage    = convertVoltage(tempData)
    windVoltage    = convertVoltage(windData)
    direcVoltage   = convertVoltage(direcData)
    temperature    = convertTemp(tempData)
    temp_F         = convertTemp(tempData)
    mph           = convertWind(windData)

    print("###-----------------------------------------------------------------##$
#    print("   Direction   bitValue = {} | Voltage = {} V |"  .format(direcData, $
    print("   Wind        bitValue = {} | Voltage = {} V | Wind  = {} MPH"  .form$
          windData, windVoltage, mph))

    print("   Light       bitValue = {} | Voltage = {} V |"  .format(lightData, l$
    print("   Temperature bitValue = {} | Voltage = {} V | Temp  = {} F"    .form$
          tempData, tempVoltage, temp_F))
 #   print("   Temperature bitValue = {} | Voltage = {} V | Temp  = {} C"    .for$
 #         tempData, tempVoltage, temperature))
 #   print("   Pressure    bitValue = {} | Voltage = {} V | inHg  = {} in"   .for$
 #         tempData, tempVoltage, temperature))

    print("###-----------------------------------------------------------------##$
    time.sleep(1)



