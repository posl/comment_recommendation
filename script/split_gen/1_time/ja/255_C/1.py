def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
        return
    elif D > 0:
        if X < A:
            print(A-X)
            return
        elif X >= A+(N-1)*D:
            print(X-A-(N-1)*D)
            return
        else:
            if (X-A) % D == 0:
                print(0)
                return
            else:
                print(min(X-A-(X-A)//D*D, A+(X-A)//D*D+D-X))
                return
    else:
        if X > A:
            print(X-A)
            return
        elif X <= A-(N-1)*D:
            print(A-X-(N-1)*D)
            return
        else:
            if (X-A) % D == 0:
                print(0)
                return
            else:
                print(min(X-A-(X-A)//D*D, A+(X-A)//D*D+D-X))
                return
