def isNineMultiple(num):
    numStr = str(num)
    sum = 0
    for i in range(len(numStr)):
        sum += int(numStr[i])
    if sum % 9 == 0:
        return True
    else:
        return False
