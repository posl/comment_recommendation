def solve():
    N,M,X,T,D = map(int,input().split())
    for i in range(X):
        T += D
    for i in range(X,N):
        T -= D
    print(T)
