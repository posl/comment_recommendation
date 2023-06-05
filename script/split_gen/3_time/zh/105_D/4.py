def getSum(A, l, r):
    sum = 0
    for i in range(l, r+1):
        sum += A[i]
    return sum
