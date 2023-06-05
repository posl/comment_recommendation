def getLine(x1,y1,x2,y2):
    if x1 == x2:
        return 'x' + str(x1)
    elif y1 == y2:
        return 'y' + str(y1)
    else:
        return 'k' + str((y2-y1)/(x2-x1)) + 'b' + str(y1 - x1*(y2-y1)/(x2-x1))

if __name__ == '__main__':
    getLine()