def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(N):
        for j in range(X + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j - A[i]] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]
    if dp[N][X] > 0:
        print("Yes")
    else:
        print("No")
