def takoyaki_fest(n, d):
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    return sum
