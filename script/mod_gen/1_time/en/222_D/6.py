def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] = (i+1)番目までの要素で、総和がjとなる場合の数
    dp = [[0] * (N * 3001 + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N * 3001 + 1):
            if j + A[i] <= N * 3000:
                dp[i + 1][j + A[i]] += dp[i][j]
                dp[i + 1][j + A[i]] %= MOD
            if j + B[i] + 1 <= N * 3000:
                dp[i + 1][j + B[i] + 1] -= dp[i][j]
                dp[i + 1][j + B[i] + 1] %= MOD
    for i in range(N):
        for j in range(N * 3001):
            dp[i + 1][j + 1] += dp[i + 1][j]
            dp[i + 1][j + 1] %= MOD
    ans = 0
    for i in range(N * 3001 + 1):
        ans += dp[N][i]
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()