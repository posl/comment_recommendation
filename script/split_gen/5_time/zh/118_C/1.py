def getGCD(x,y):
    if y == 0:
        return x
    else:
        return getGCD(y,x%y)
