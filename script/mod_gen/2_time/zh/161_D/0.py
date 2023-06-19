def isLuckyNumber(x):
    x = str(x)
    for i in range(1,len(x)):
        if abs(int(x[i])-int(x[i-1]))>1:
            return False
    return True

if __name__ == '__main__':
    isLuckyNumber()