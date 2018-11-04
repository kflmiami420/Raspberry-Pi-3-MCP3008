import time
import spidev

spi = spidev.SpiDev()
spi.open(0,0)

tempChannel    = 1
windChannel    = 2

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

def convertWind(bitValue, decimalPlaces=4):
    windms            = ((bitValue * 3.3) / float(1023)- .005)
    windms2           = ((windms - 0.4) * 20.25)
    mph               = (windms2 * 2.237136)
    mph               = round(mph, decimalPlaces)
    return  mph

while True:

    tempData       = getReading(tempChannel)
    windData       = getReading(windChannel)
    speedData      = getReading(windChannel)
    tempVoltage    = convertVoltage(tempData)
    windVoltage    = convertVoltage(windData)
    temperature    = convertTemp(tempData)
    temp_F         = convertTemp(tempData)
    mph           = convertWind(windData)

    print("###-----------------------------------------------------------------###")
    print("   Wind        bitValue = {} | Voltage = {} V | Wind  = {} MPH"  .format(\
          windData, windVoltage, mph))
    print("   Temperature bitValue = {} | Voltage = {} V | Temp  = {} F"    .format(\
          tempData, tempVoltage, temp_F))
    print("###-----------------------------------------------------------------###")
    time.sleep(1)

