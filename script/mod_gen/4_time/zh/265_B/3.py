def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    X = [i[0] for i in XY]
    Y = [i[1] for i in XY]
    for i in range(N-1):
        if i+1 in X:
            T += Y[X.index(i+1)]
        T -= A[i]
        if T <= 0:
            print("No")
            return
    print("Yes")
solve()
