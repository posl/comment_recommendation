def problem():
    N,M,X,T,D = map(int,input().split())
    height = T
    for i in range(1,M):
        height += D
    for i in range(M,X):
        height += D
    for i in range(X,N):
        height += 0
    return height
print(problem())

if __name__ == '__main__':
    problem()