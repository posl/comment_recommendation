def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # dp[i][j] := i番目までの数字を用いて、jを作るための組み合わせの数
    dp = [[0] * (N * 3000 + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N * 3000 + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] += dp[i][j - A[i]]
            if j - B[i] - 1 >= 0:
                dp[i + 1][j] -= dp[i][j - B[i] - 1]
            dp[i + 1][j] += dp[i + 1][j - 1]
            dp[i + 1][j] %= 998244353
    print(dp[N][N * 3000])
