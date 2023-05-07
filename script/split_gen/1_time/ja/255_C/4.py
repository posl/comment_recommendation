def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
        return
    if D > 0:
        if X < A:
            print(abs(X-A))
            return
        if X > A + D*(N-1):
            print(abs(X-A-D*(N-1)))
            return
        if (X-A)%D == 0:
            print(0)
        else:
            if (X-A)//D < N-1:
                print(min(abs(X-A-D*((X-A)//D+1)),abs(X-A-D*((X-A)//D))))
            else:
                print(abs(X-A-D*((X-A)//D)))
    if D < 0:
        if X > A:
            print(abs(X-A))
            return
        if X < A + D*(N-1):
            print(abs(X-A-D*(N-1)))
            return
        if (X-A)%D == 0:
            print(0)
        else:
            if (X-A)//D < N-1:
                print(min(abs(X-A-D*((X-A)//D+1)),abs(X-A-D*((X-A)//D))))
            else:
                print(abs(X-A-D*((X-A)//D)))
