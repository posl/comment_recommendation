def main():
    N,M,X,T,D = map(int,input().split())
    h = T
    for i in range(1,X):
        h += D
    for i in range(X,N):
        h += D
    print(h)

if __name__ == '__main__':
    main()