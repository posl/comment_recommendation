def main():
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]
    mod = 998244353
    dp = [0]*(n+1)
    dp[1] = 1
    s = [0]*(n+1)
    s[1] = 1
    for i in range(2, n+1):
        for l, r in lr:
            if i-l < 0:
                continue
            if i-r-1 >= 0:
                dp[i] += s[i-l]-s[i-r-1]
            else:
                dp[i] += s[i-l]
        dp[i] %= mod
        s[i] = s[i-1]+dp[i]
    print(dp[n])

if __name__ == '__main__':
    main()