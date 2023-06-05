def isLuckyNum(num):
    numStr = str(num)
    for i in range(len(numStr)-1):
        if abs(int(numStr[i])-int(numStr[i+1])) > 1:
            return False
    return True
