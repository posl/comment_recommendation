def main():
    pass
    n,m = map(int,input().split())
    a = [int(input()) for _ in range(m)]
    mod = 10**9+7
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= mod
    print(dp[n])

if __name__ == '__main__':
    main()