def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    # dp[i][j] = i番目までのチーズで重さj以下のときの最大のおいしさ
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    # print(dp)
    for i in range(N):
        for j in range(W + 1):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - B[i]] + A[i])
            else:
                dp[i + 1][j] = dp[i][j]
    # print(dp)
    print(dp[N][W])
