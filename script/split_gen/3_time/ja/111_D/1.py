def solve():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if X[0] != 0 or Y[0] != 0:
        print(-1)
        return
    for i in range(1, N):
        if abs(X[i] - X[i - 1]) + abs(Y[i] - Y[i - 1]) > 40:
            print(-1)
            return
    m = 40
    d = [1] * m
    for i in range(m):
        d[i] = 2 ** (m - i - 1)
    print(m)
    print(*d)
    for i in range(N):
        w = ""
        for j in range(m):
            if X[i] & (1 << (m - j - 1)):
                w += "R"
            else:
                w += "L"
            if Y[i] & (1 << (m - j - 1)):
                w += "U"
            else:
                w += "D"
        print(w)
