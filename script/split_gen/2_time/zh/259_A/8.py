def birthday():
    N,M,X,T,D = map(int, input().split())
    height = T
    for i in range(1, X):
        height += D
    for i in range(X, M):
        height += D
    print(height)
