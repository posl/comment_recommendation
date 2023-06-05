def getAB(x):
    if x == 1:
        return 0,-1
    else:
        for a in range(1,1000):
            for b in range(1,1000):
                if a**5-b**5 == x:
                    return a,b

if __name__ == '__main__':
    getAB()