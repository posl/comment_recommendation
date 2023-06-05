def getGCD(x,y):
    if y == 0:
        return x
    else:
        return getGCD(y,x%y)

if __name__ == '__main__':
    getGCD()