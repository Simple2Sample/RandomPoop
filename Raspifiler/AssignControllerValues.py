import ControllerVariables

def assign_ValueToButtons(inputStruct):
    HiDCode = inputStruct.code
    HiDValue = inputStruct.value
    
    #ControllerVariables.code[HiDCode] = HiDValue
    if not (HiDCode == 0 and HiDValue == 0):
        ControllerVariables.code[HiDCode] = HiDValue
        #print(ControllerVariables.code[1])
        #print('code', HiDCode,'value',HiDValue)