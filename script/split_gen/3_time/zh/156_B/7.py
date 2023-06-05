def getNumOfDigits(number, base):
    numOfDigits = 0
    while number > 0:
        number = number // base
        numOfDigits += 1
    return numOfDigits
