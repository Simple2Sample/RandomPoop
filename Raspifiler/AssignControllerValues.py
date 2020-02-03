import ControllerVariables

def assign_ValueToButtons(inputStruct):
    HiDCode = inputStruct.code
    HiDValue = inputStruct.value
    
    print('code', HiDCode,'value',HiDValue)

    ControllerVariables.code[HiDCode] = HiDValue
 
"""if HiDCode == 0 :
    ControllerVariables.xAxis1 = HiDValue
elifHiDCode == 0 :
    ControllerVariables.xAxis1 = HiDValue
elif
    """