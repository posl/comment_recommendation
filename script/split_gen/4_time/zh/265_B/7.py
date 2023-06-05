def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    XY.sort()
    X, Y = zip(*XY)
    X = list(X)
    Y = list(Y)
    X.append(N)
    Y.append(0)
    now = 0
    for i in range(M+1):
        d = X[i] - now
        T -= d
        if T <= 0:
            print("No")
            exit()
        T += Y[i]
        T = min(T, A[i])
        now = X[i]
    print("Yes")
