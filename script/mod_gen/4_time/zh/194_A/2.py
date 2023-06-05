def getIceType(A,B):
    if A >= 15 and B >= 8:
        return 1
    elif A >= 10 and B >= 3:
        return 2
    elif A >= 3:
        return 3
    else:
        return 4

if __name__ == '__main__':
    getIceType()