def main():
    # input
    N,M,X,T,D = map(int, input().split())
    # compute
    height = T
    for i in range(1, X):
        height -= D
    for i in range(X, M):
        height += D
    for i in range(M, N):
        pass
    # output
    print(height)
