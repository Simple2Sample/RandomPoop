import serial
import ControllerVariables
from time import sleep
messageLength = 10000   #Specifies how much of the decimal number we want to transfer to MyRio
ser = serial.Serial("/dev/ttyS0",115200)
def sendMSG(message):
    for x in range (0, len(message)):
        convertedMessage = int(message[x]*messageLength)
        print(len(str(convertedMessage)))
        ser.write(convertedMessage)
    


    
















""" #Enables SPI in script
    spi = spidev.SpiDev()
    #Opens SPI module 0 and device 0
    spi.open(0,0)
    spi.max_speed_hz = 20000000
    spi.wxfer3(message*1000[, 20000000, 20, 8])
    print(69)"""