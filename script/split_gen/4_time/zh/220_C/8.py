def getSum(A, X):
    B = []
    for i in range(100):
        B.extend(A)
    #print(B)
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            return i+1
    return -1
