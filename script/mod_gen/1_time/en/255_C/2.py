def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
    else:
        if D > 0:
            if X < A:
                print(abs(X-A))
            elif X > A+(N-1)*D:
                print(abs(X-(A+(N-1)*D)))
            else:
                print(0)
        else:
            if X > A:
                print(abs(X-A))
            elif X < A+(N-1)*D:
                print(abs(X-(A+(N-1)*D)))
            else:
                print(0)

if __name__ == '__main__':
    main()