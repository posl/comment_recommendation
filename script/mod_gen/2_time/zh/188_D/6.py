def getSecondPlace(a):
    n = len(a)
    if n == 2:
        return a[0] if a[0] < a[1] else a[1]
    else:
        left = a[:n//2]
        right = a[n//2:]
        leftSecond = getSecondPlace(left)
        rightSecond = getSecondPlace(right)
        return leftSecond if leftSecond < rightSecond else rightSecond

if __name__ == '__main__':
    getSecondPlace()