def getDistinctIntegerCount():
    inputString = input()
    distinctIntegerSet = set()
    for integer in inputString.split():
        distinctIntegerSet.add(integer)
    print(len(distinctIntegerSet))
getDistinctIntegerCount()
