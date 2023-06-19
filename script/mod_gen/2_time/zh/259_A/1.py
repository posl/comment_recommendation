def main():
    N,M,X,T,D = map(int,input().split())
    for i in range(1,N+1):
        if i == M:
            print(X)
            break
        elif i < X:
            X += D
        else:
            X += D

if __name__ == '__main__':
    main()