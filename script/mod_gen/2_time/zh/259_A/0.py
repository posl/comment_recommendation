def birthday(N,M,X,T,D):
    height = T
    for i in range(X,M):
        height += D
    return height

if __name__ == '__main__':
    birthday()