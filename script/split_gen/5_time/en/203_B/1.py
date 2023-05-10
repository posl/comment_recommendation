def calcSum(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += int(str(i) + '0' + str(j))
    return sum
