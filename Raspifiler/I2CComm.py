import serial
import ControllerVariables
from time import sleep

ser = serial.Serial("/dev/ttyS0",230400)
def sendMSG(message):
     #Specifies how much of the decimal number we want to transfer to MyRio
    for x in range (0, len(message)):
        messageLength = 100000000000000000
        convertedMessage = int(message[x]*messageLength)
        convertedMessage = str(convertedMessage)
        
        #print(int(message[x]*messageLength))
        
        #convertedMessage = convertedMessage
        #print((convertedMessage))
        messageLength = str(messageLength)
        print(len(messageLength.encode('utf-8')))
        print(len((bytes(convertedMessage.encode('utf-8')))))
        convertedMessage = '0'*(len(messageLength)-len(convertedMessage)) + convertedMessage
        print(bytes(convertedMessage.encode('utf-8')))

        ser.write(bytes(convertedMessage.encode('utf-8')))
        