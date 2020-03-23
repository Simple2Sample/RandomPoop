import ControllerVariables
import FindController
import math
import I2CComm
yAxis = ControllerVariables.code[1]
xAxis = ControllerVariables.code[0]
#Extracts the axis values from ControllerVariables
xAxisRotation = ControllerVariables.code[3]
yAxisRotation = ControllerVariables.code[4]
#DO NOT USE THIS CODE! OLD
rate = 0.4 
curveLength = 0.5 #Length of one section
length = 0.035 

#Makes sure the joystick value is between 1 and -1
def JoyStickCorrector(axisValue, rate):
   correction = axisValue / 32767
   mixup = correction * rate
   if mixup < 1 and mixup > -1:
       return mixup
    

#
def FindK (axisValue, rate, ranger):
    rangeValue = ranger * math.pi
    correction = JoyStickCorrector (axisValue, 2*rate)
    if correction < rangeValue and correction > (-1)*rangeValue:
        return correction

def InverseKinematicWire (k, phi, s):
    first = s*(1-k*length*math.cos(((math.pi)/6)) + phi)
    second = s*(1+k*length*math.sin(((math.pi)/3)) + phi)
    third = s*(1-k*length*math.sin(phi))
    L1 = first - length
    L2 = second - length
    L3 = third - length
    wirelength = [L1,L2,L3]
    return wirelength


def CalculateKinematics():
    phi1 = JoyStickCorrector (xAxis, rate)
    phi2 = JoyStickCorrector (xAxisRotation, rate)
    k1   = FindK(yAxis, rate, 0.7)
    k2   = FindK(yAxisRotation,rate,1.2)
    
    #sendMessageSPI = [phi1,phi2,k1,k2]
    
    #Turns the kinematic values into a list and sends them to MyRio 
    #I2CComm.sendMSG(sendMessageSPI)
    firstThreeWires = InverseKinematicWire(k1,phi1,length)
    lastThreeWires =  InverseKinematicWire(k2,phi2,length)
    wirelengths = firstThreeWires + lastThreeWires
    return wirelengths