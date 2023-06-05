def getPoint(A,B):
    # x = A / (A + B)
    # y = B / (A + B)
    x = 1 / (1 + B / A)
    y = 1 / (1 + A / B)
    return x,y

if __name__ == '__main__':
    getPoint()