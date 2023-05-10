def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    # dp[i][j] = i番目までの要素からj個選んで平均値が整数になる場合の数
    dp = [[0 for _ in range(10000)] for _ in range(101)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(10000):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            dp[i+1][j+a[i]] += dp[i][j]
            dp[i+1][j+a[i]] %= mod
    ans = 0
    for i in range(1, n+1):
        ans += dp[i][i*sum(a)//n]
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()