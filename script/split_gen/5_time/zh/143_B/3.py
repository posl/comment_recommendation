def sum_healths(n,ds):
    sum = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            sum += ds[i]*ds[j]
    return sum
