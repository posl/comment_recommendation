def getBlueCount(n, a, b):
    if a == 0:
        return 0
    if b == 0:
        return n
    if a + b >= n:
        return a
    else:
        return a + (n - a - b)

if __name__ == '__main__':
    getBlueCount()