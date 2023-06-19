def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    XY.sort()
    X = [x for x, _ in XY]
    Y = [y for _, y in XY]
    if X[0] != 1:
        print("No")
        return
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        if i+1 in X:
            t += Y[X.index(i+1)]
            if t > T:
                t = T
    print("Yes")

if __name__ == '__main__':
    solve()