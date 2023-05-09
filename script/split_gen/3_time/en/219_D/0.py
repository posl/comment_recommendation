def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[float("inf") for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[i+1][j+A[i]][k+B[i]] = min(dp[i+1][j+A[i]][k+B[i]], dp[i][j][k]+1)
    ans = dp[N][X][Y]
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)
