import ControllerVariables
import FindController
import math
yAxis = ControllerVariables.code[1]
xAxis = ControllerVariables.code[0]

xAxisRotation = ControllerVariables.code[3]
yAxisRotation = ControllerVariables.code[4]

rate = 0.4
curveLength = 1
length = 0.035

def JoyStickCorrector(axisValue, rate):
   correction = axisValue / 32767
   mixup = correction * rate
   if mixup < 1 and mixup > -1:
       return mixup
    


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
    return wirelength[L1, L2,L3]


def CalculateKinematics():
    phi1 = JoyStickCorrector (xAxis, rate)
    phi2 = JoyStickCorrector (xAxisRotation, rate)
    k1   = FindK(yAxis, rate, 0.7)
    k2   = FindK(yAxisRotation,rate,1.2)

    firstThreeWires = InverseKinematicWire(k1,phi1,length)
    lastThreeWires =  InverseKinematicWire(k2,phi2,length)
    wirelengths = firstThreeWires + lastThreeWires
    return wirelengths