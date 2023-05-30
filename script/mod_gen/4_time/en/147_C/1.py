def solve():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        X.append([])
        Y.append([])
        for j in range(A[i]):
            x, y = [int(_) for _ in input().split()]
            X[i].append(x-1)
            Y[i].append(y)
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if i & (1 << j):
                for k in range(A[j]):
                    if Y[j][k] == 1 and i & (1 << X[j][k]):
                        continue
                    elif Y[j][k] == 0 and i & (1 << X[j][k]) == 0:
                        continue
                    else:
                        ok = False
                        break
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)
solve()
