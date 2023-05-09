def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[0] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if dp[i][j][k] == 0:
                    continue
                if j + A[i] <= X:
                    dp[i + 1][j + A[i]][k] = 1
                if k + B[i] <= Y:
                    dp[i + 1][j][k + B[i]] = 1
    for i in range(1, N + 1):
        if dp[i][X][Y] == 1:
            print(i)
            return
    print(-1)
    return
