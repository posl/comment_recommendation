def main():
    N,M,X,T,D = map(int,input().split())
    for i in range(1,N+1):
        if i == M:
            print(X)
        else:
            X = X+D
    return 0

if __name__ == '__main__':
    main()