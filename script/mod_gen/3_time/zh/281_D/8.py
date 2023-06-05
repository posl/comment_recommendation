def getSum(k, d, a):
    if k == 1:
        return 0
    if k == 2:
        return a[0] + a[1]
    if k == 3:
        if a[0] % d == 0:
            return a[1] + a[2]
        if a[1] % d == 0:
            return a[0] + a[2]
        if a[2] % d == 0:
            return a[0] + a[1]
        return -1
    return -1

if __name__ == '__main__':
    getSum()