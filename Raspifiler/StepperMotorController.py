




def amountOfSteps(currentPosition):
    position = currentPosition
    
    #corrects position value to be between 0.08 and -0.08
    if position > 0.08:
        position = 0.08
    elif position < -0.08:
        position = -0.08
    position = (position / 0.005)*200
    return(round(position))

def clusterCalculations (clusterOne, clusterTwo, absoluteLengths):
    firstCluster = clusterOne/max(clusterOne)
    secondCluster = clusterTwo/max(clusterTwo)
    combinedCluster = [secondCluster[1],firstCluster[2], secondCluster[3], absoluteLengths[4], firstCluster[1], secondCluster[2], absoluteLengths[8]]
    return combinedCluster
def wireLengthToValue(wirelengths):
    

    steps = amountOfSteps(0)
    convertedLengths = [x-steps for x in wirelengths]
    absLengths = abs(convertedLengths)

    firstCluster = [absLengths[5],absLengths[2],absLengths[7]]
    secondCluster = [absLengths[1],absLengths[6],absLengths[3]]
    
    clusterLogic = clusterCalculations (firstCluster, secondCluster, absLengths)
    lengthCalculationsDone = [0,0,0,0,0,0,0,0]

    for x in lengthCalculationsDone:
        lengthCalculationsDone[x] = 1/clusterLogic[x]
    
    