def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] := Aのi番目までの要素を使って、jを作る場合の数
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
    ans = 0
    for i in range(N):
        ans += dp[N][i + 1] * (B[i] - A[i] + 1)
        ans %= MOD
    print(ans)
