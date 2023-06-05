def getScore(a,b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b + 1
    elif b == 0:
        return a + 1
    else:
        return a + b + 1

if __name__ == '__main__':
    getScore()