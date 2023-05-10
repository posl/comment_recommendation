def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] = i番目までの数字を使ってjを作る組み合わせの総数
    dp = [[0] * (sum(A)+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(sum(A)+1):
            dp[i+1][j] += dp[i][j]
            if j + A[i] < sum(A)+1:
                dp[i+1][j+A[i]] += dp[i][j]
            dp[i+1][j] %= MOD
            dp[i+1][j+A[i]] %= MOD
    ans = 0
    for i in range(1, sum(A)+1):
        if i % N == 0:
            ans += dp[N][i]
    print(ans % MOD)

if __name__ == '__main__':
    main()