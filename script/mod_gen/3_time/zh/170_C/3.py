def getClosestNum(x, p):
    if len(p) == 0:
        return x
    else:
        minNum = 100
        for i in range(0, len(p)):
            if abs(x - p[i]) < minNum:
                minNum = abs(x - p[i])
                result = p[i]
        return result

if __name__ == '__main__':
    getClosestNum()