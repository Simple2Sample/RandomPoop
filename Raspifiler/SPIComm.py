import spidev
import ControllerVariables
def sendMSG(message)

    #Enables SPI in script
    spi = spidev.SpiDev()
    #Opens SPI module 0 and device 0
    spi.open(0,0)
    spi.max_speed_hz = 100
    spi.writebytes2(ControllerVariables.code)
