def getGoodNum(n, w, a):
    a.sort()
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > w:
            return i
    return n
