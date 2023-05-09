def getBlueJewels(n, x, y):
    if n == 1:
        return 0
    elif x >= y:
        return getBlueJewels(n-1, x, y) + x
    else:
        return max(getBlueJewels(n-1, x, y) + x, getBlueJewels(n-1, x, y) + y)

if __name__ == '__main__':
    getBlueJewels()