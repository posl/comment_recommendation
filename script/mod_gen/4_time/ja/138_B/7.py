def getInverseSum(n, a):
    sum = 0
    for i in range(n):
        sum += 1/a[i]
    return 1/sum

if __name__ == '__main__':
    getInverseSum()