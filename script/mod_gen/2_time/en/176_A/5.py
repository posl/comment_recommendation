def takoyaki(N,X,T):
    count = 0
    while N > 0:
        N -= X
        count += T
    return count
N,X,T = list(map(int,input().split()))
print(takoyaki(N,X,T))
