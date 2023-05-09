def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        print(abs(X-A))
        return
    elif D > 0:
        if X < A:
            print(A-X)
        elif X > A+(N-1)*D:
            print(X-(A+(N-1)*D))
        else:
            print(min(X-A,(A+(N-1)*D)-X))
    else:
        if X > A:
            print(X-A)
        elif X < A+(N-1)*D:
            print((A+(N-1)*D)-X)
        else:
            print(min(A-X,X-(A+(N-1)*D)))

if __name__ == '__main__':
    main()