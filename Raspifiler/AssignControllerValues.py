import ControllerVariables

def assign_ValueToButtons(inputStruct):
    HiDCode = inputStruct.code
    HiDValue = inputStruct.value
    
    print('code', HiDCode,'value',HiDValue)

    if HiDCode == 0:
        ControllerVariables.code0 = HiDValue
    elif HiDCode == 1:
        ControllerVariables.code1 = HiDValue
    elif HiDCode == 2:
        ControllerVariables.code2 = HiDValue
    elif HiDCode == 3:
        ControllerVariables.code3 = HiDValue
    elif HiDCode == 4:
        ControllerVariables.code4 = HiDValue
    elif HiDCode == 5:
        ControllerVariables.code5 = HiDValue
    elif HiDCode == 16:
        ControllerVariables.code16 = HiDValue
    elif HiDCode == 17:
        ControllerVariables.code17 = HiDValue
    elif HiDCode == 304:
        ControllerVariables.code304 = HiDValue
    elif HiDCode == 305:
        ControllerVariables.code305 = HiDValue
    elif HiDCode == 306:
        ControllerVariables.code306 = HiDValue
    elif HiDCode == 307:
        ControllerVariables.code307 = HiDValue
    elif HiDCode == 310:
        ControllerVariables.code310 = HiDValue
    elif HiDCode == 311:
        ControllerVariables.code311 = HiDValue
 
"""if HiDCode == 0 :
    ControllerVariables.xAxis1 = HiDValue
elifHiDCode == 0 :
    ControllerVariables.xAxis1 = HiDValue
elif
    """