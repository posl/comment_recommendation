def solve():
    N = int(input())
    A = [0] * N
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        A[i] = int(input())
        X[i] = [0] * A[i]
        Y[i] = [0] * A[i]
        for j in range(A[i]):
            X[i][j], Y[i][j] = map(int, input().split())
            X[i][j] -= 1
    ans = 0
    for mask in range(1 << N):
        ok = True
        for i in range(N):
            if mask & (1 << i):
                for j in range(A[i]):
                    if ((mask >> X[i][j]) & 1) ^ Y[i][j]:
                        ok = False
                        break
                if not ok:
                    break
        if ok:
            ans = max(ans, bin(mask).count('1'))
    print(ans)
