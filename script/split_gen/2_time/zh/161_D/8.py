def isLuckyNumber(num):
    numStr = str(num)
    for i in range(1, len(numStr)):
        if abs(int(numStr[i]) - int(numStr[i-1])) > 1:
            return False
    return True
