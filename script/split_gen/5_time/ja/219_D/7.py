def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0] * (Y + 1) for _ in range(X + 1)]
    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[j + A[i]][k + B[i]] = max(dp[j + A[i]][k + B[i]], dp[j][k] + 1)
    if dp[X][Y] == 0:
        print(-1)
    else:
        print(dp[X][Y])
