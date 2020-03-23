import serial
import ControllerVariables
from time import sleep

ser = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_7563031353635120D0A2-if00',28800) #ttyACMx changes value sometimes. See which port Arduino is connected to.
def sendMSG(message):
    #Specifies how much of the decimal number we want to transfer to MyRio
    print(len(message))
    startMessage = 'X'
    ser.write(bytes(startMessage.encode('utf-8')))
    for x in range(len(message)):
        messageLength = 10000
        convertedMessage = round(message[x]*messageLength)
        convertedMessage = str(convertedMessage)
        
        #print(int(message[x]*messageLength))
        
        #convertedMessage = convertedMessage
        #print((convertedMessage))
        messageLength = str(messageLength)
        print(len(messageLength.encode('utf-8')))
        print(len((bytes(convertedMessage.encode('utf-8')))))

        if ('-' in convertedMessage): #Moves the '-' character to the front of the string.
            convertedMessage = convertedMessage.replace('-','')
            convertedMessage = '0'*(len(messageLength)-len(convertedMessage)) + convertedMessage #Adds a 0 at the start of the message to ensure all the messages have the same length
            convertedMessage = 'N' + convertedMessage
        else:
            convertedMessage = '0'*(len(messageLength)-len(convertedMessage)) + convertedMessage #Adds a 0 at the start of the message to ensure all the messages have the same length
            convertedMessage = 'P'+ convertedMessage



        convertedMessage = '0'*(len(messageLength)-len(convertedMessage)) + convertedMessage #Adds a 0 at the start of the message to ensure all the messages have the same length
        print(len((bytes(convertedMessage.encode('utf-8')))))
        print(bytes(convertedMessage.encode('utf-8')))

        ser.write(bytes(convertedMessage.encode('utf-8')))
        