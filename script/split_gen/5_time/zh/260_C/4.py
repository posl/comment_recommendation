def getN1(n,x,y):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getN1(n-1,x,y) + x * getN2(n-1,x,y)
