def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(n + 1)]
        dp[0][0] = 1
        for j in range(n):
            for k in range(10):
                dp[j + 1][(k + a[j]) % 10] += dp[j][k]
                dp[j + 1][(k + a[j]) % 10] %= mod
                dp[j + 1][(k * a[j]) % 10] += dp[j][k]
                dp[j + 1][(k * a[j]) % 10] %= mod
        ans[i] = dp[-1][i]
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()