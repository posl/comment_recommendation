def getAB(x):
    for a in range(100):
        for b in range(100):
            if a**5-b**5==x:
                return a,b
    return None
