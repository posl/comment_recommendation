def solve():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if A == X:
            print(0)
        else:
            print(N)
        return
    if N == 1:
        if A == X:
            print(0)
        else:
            print(1)
        return
    if D > 0:
        if A > X:
            print(N)
            return
        if A + D * (N - 1) < X:
            print(N)
            return
        if (X - A) % D == 0:
            print(0)
            return
        else:
            print(1)
            return
    if D < 0:
        if A < X:
            print(N)
            return
        if A + D * (N - 1) > X:
            print(N)
            return
        if (X - A) % D == 0:
            print(0)
            return
        else:
            print(1)
            return
solve()
