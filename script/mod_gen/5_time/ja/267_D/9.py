def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # dp[i][j] := i番目までの要素からj個選んだときのsum_{i=1}^{j} i × B_iの最大値
    # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + i * A[i - 1])
    dp = [[-float('inf')] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if j > i:
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + i * A[i - 1])
    print(dp[N][M])

if __name__ == '__main__':
    solve()