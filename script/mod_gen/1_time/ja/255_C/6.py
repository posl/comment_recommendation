def main():
    X,A,D,N=map(int,input().split())
    if D==0:
        print(abs(X-A))
    elif D>0:
        if X<A:
            print(A-X)
        elif X>A+D*(N-1):
            print(X-(A+D*(N-1)))
        else:
            print(min(X-A,A+D*(N-1)-X))
    else:
        if X>A:
            print(X-A)
        elif X<A+D*(N-1):
            print(A+D*(N-1)-X)
        else:
            print(min(X-A,A+D*(N-1)-X))

if __name__ == '__main__':
    main()