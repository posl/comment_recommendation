def problems203_b(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += i*100+j
    return sum
n,k = map(int,input().split())
print(problems203_b(n,k))
