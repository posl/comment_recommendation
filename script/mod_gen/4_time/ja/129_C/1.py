def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    mod = 10**9+7
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n):
        if i+1 in a:
            continue
        if i+1 <= n:
            dp[i+1] += dp[i]
            dp[i+1] %= mod
        if i+2 <= n:
            dp[i+2] += dp[i]
            dp[i+2] %= mod
    print(dp[-1])

if __name__ == '__main__':
    main()