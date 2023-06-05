def getSumOfHealthPoints(N, d):
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    print(sum)
