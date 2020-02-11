import ControllerVariables
import math
import I2CComm

rate = 0.4
curveLength = 0.5
length = 0.035

def JoyStickCorrector(axisValue, rate):
   #Corrects the joystick input to between 1 and -1.
    #Deadzone correction has not been implemented.
   correction = axisValue / 32767
   mixup = correction * rate
   if mixup < 1 and mixup > -1:
       return mixup
   elif mixup > 1:
       return 1
   elif mixup < 1:
       return -1
    


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
    wirelength = [L1, L2,L3]
    return wirelength


def CalculateKinematics():
    
    yAxis = ControllerVariables.code[1]
    xAxis = ControllerVariables.code[0]
    #print(xAxis)
    xAxisRotation = ControllerVariables.code[2]
    yAxisRotation = ControllerVariables.code[5]
    
    phi1 = JoyStickCorrector (xAxis, rate)
    phi2 = JoyStickCorrector (xAxisRotation, rate)
    k1   = FindK(yAxis, rate, 0.7)
    k2   = FindK(yAxisRotation,rate,1.2)
    kinematicsVariables = [phi1,phi2,k1,k2]
    I2CComm.sendMSG(kinematicsVariables)
    firstThreeWires = InverseKinematicWire(k1,phi1,length)
    lastThreeWires =  InverseKinematicWire(k2,phi2,length)
    wirelengths = firstThreeWires + lastThreeWires    
    return wirelengths