def getSubordinateNumber(n, a):
    subordinateNumber = [0] * n
    for i in range(n - 1):
        subordinateNumber[a[i] - 1] += 1
    return subordinateNumber

if __name__ == '__main__':
    getSubordinateNumber()