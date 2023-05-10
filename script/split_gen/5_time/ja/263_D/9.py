def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    # dp[i][0]: i番目までの要素を操作したときの最小値
    # dp[i][1]: i番目までの要素を操作したときの最大値
    dp = [[0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        # dp[i][0]を求める
        # dp[i - 1][0] + A[i] + L
        # dp[i - 1][1] + A[i] + L
        # dp[i - 1][0] + A[i] + R
        # dp[i - 1][1] + A[i] + R
        dp[i][0] = min(dp[i - 1][0] + A[i] + L, dp[i - 1][1] + A[i] + L, dp[i - 1][0] + A[i] + R, dp[i - 1][1] + A[i] + R)
        # dp[i][1]を求める
        # dp[i - 1][0] + A[i] + L
        # dp[i - 1][1] + A[i] + L
        # dp[i - 1][0] + A[i] + R
        # dp[i - 1][1] + A[i] + R
        dp[i][1] = max(dp[i - 1][0] + A[i] + L, dp[i - 1][1] + A[i] + L, dp[i - 1][0] + A[i] + R, dp[i - 1][1] + A[i] + R)
    print(dp[N][0])
