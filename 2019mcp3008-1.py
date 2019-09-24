#2019 September 24 2019 python3 tested mcp3008 , 10k pot , tmp36 temp sensor on rapberry pi 4 debian buster
import time
import spidev
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
spi = spidev.SpiDev()
spi.open(0,0)

tempChannel    = 3
windChannel    = 0

def getReading(channel):
    rawData = spi.xfer([1, (8 + channel) << 4, 0])
    processedData = ((rawData[1]&3) << 8) + rawData[2]
    return processedData

def convertVoltage(bitValue, decimalPlaces=3):
    voltage = (bitValue * 3.3) / float(1023)
    voltage = round(voltage, decimalPlaces)
    return voltage

def convertTemp(bitValue, decimalPlaces=0):
    temperature        = ((bitValue * 330)/float(1023) - 50)
    temperature        = ((temperature * 9/5) + 32)
    temperature        = round(temperature, decimalPlaces)
    return temperature

def convertWind(bitValue, decimalPlaces=2):
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
    mph           = convertWind(windData)

    print("###-----------------------------------------------------------------###")
    print("   Wind        bitValue = {} | Voltage = {} V | Wind  = {} MPH"  .format(\
          windData, windVoltage, mph))
    print("   Temperature bitValue = {} | Voltage = {} V | Temp  = {} F"    .format(\
          tempData, tempVoltage, temperature))
    print("###-----------------------------------------------------------------###")
    time.sleep(1)



