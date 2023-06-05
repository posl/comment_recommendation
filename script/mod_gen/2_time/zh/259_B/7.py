def main():
    N,M,X,T,D = map(int,input().split())
    height = T
    for i in range(1,M):
        height += D
    for i in range(M,N):
        height += D
        if i == X:
            height -= D
    print(height)

if __name__ == '__main__':
    main()