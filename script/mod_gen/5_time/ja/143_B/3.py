def getSumOfTakoyakiPower(takoyakiPowerList):
    sumOfTakoyakiPower = 0
    for i in range(len(takoyakiPowerList)):
        for j in range(i+1,len(takoyakiPowerList)):
            sumOfTakoyakiPower = sumOfTakoyakiPower + takoyakiPowerList[i] * takoyakiPowerList[j]
    return sumOfTakoyakiPower

if __name__ == '__main__':
    getSumOfTakoyakiPower()