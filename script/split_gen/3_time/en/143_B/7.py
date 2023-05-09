def takoyaki():
    n = int(input())
    d = [int(x) for x in input().split()]
    sum = 0
    for i in range(n):
        for j in range(i+1,n):
            sum += d[i] * d[j]
    return sum
print(takoyaki())
