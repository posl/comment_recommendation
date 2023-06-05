def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        print(0)
        return
    if D > 0:
        if X < A:
            print(A-X)
            return
        else:
            if (X-A)%D == 0:
                print((X-A)//D)
                return
            else:
                print(-1)
                return
    if D < 0:
        if X > A:
            print(X-A)
            return
        else:
            if (A-X)%(-D) == 0:
                print((A-X)//(-D))
                return
            else:
                print(-1)
                return

if __name__ == '__main__':
    main()