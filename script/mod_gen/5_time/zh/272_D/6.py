def getMoveCount(x,y):
    if x == y:
        return x
    elif x > y:
        return x
    else:
        return y

if __name__ == '__main__':
    getMoveCount()