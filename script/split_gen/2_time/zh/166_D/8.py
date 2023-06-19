def getAB(x):
    for a in range(0, 1000):
        for b in range(-1000, 1000):
            if a**5 - b**5 == x:
                return a, b
