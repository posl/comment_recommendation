def getClosestNum(x, p):
    #print("x", x)
    #print("p", p)
    if len(p) == 0:
        return x
    minDiff = abs(x-p[0])
    minNum = p[0]
    for i in range(1, len(p)):
        diff = abs(x-p[i])
        if diff < minDiff:
            minDiff = diff
            minNum = p[i]
    return minNum

if __name__ == '__main__':
    getClosestNum()