def main():
    X,A,D,N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
        return
    if X == A:
        print(0)
        return
    if D < 0:
        A, D = -A, -D
        X = -X
    if X < A:
        print((A-X)//D if (A-X)%D == 0 else (A-X)//D+1)
    else:
        print((X-A)//D+1 if (X-A)%D == 0 else (X-A)//D+2)
