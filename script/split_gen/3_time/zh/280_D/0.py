def getFactorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * getFactorial(n-1)
