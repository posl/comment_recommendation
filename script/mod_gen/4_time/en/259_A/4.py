def height(N,M,X,T,D):
    h = T
    for i in range(1,X):
        h += D
    for i in range(X,N):
        h += D
    return h

if __name__ == '__main__':
    height()