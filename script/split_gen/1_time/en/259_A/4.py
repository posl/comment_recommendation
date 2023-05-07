def solve():
    N,M,X,T,D = [int(x) for x in input().split()]
    height = T
    for i in range(1,X):
        height += D
    for i in range(X,N):
        height += D
    print(height)
