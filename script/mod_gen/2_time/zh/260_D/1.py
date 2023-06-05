def getBlueStoneCount(redStoneCount, x, y):
    if redStoneCount == 1:
        return 0
    if redStoneCount == 2:
        return x
    else:
        return getBlueStoneCount(redStoneCount - 1, x, y) + getBlueStoneCount(redStoneCount - 2, x, y) + y

if __name__ == '__main__':
    getBlueStoneCount()