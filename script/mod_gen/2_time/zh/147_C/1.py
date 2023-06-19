def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    X = []
    Y = []
    for i in range(N):
        X.append([])
        Y.append([])
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x - 1)
            Y[i].append(y)
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if ((i >> X[j][k]) & 1) ^ Y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)
solve()
