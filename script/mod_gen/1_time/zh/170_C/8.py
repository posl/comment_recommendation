def findClosestNumber(x, n, p):
    if n == 0:
        return x
    if x in p:
        return findClosestNumber(x + 1, n, p)
    else:
        return x

if __name__ == '__main__':
    findClosestNumber()