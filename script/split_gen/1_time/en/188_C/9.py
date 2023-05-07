def getSecondPlace(n, a):
    #print(n, a)
    first = max(a[0:2**n])
    second = max(a[2**n:])
    return a.index(second) + 1
