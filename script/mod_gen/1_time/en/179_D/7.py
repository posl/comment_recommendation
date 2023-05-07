def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    s = [0] * (N+1)
    for i in range(1, N+1):
        s[i] = s[i-1] + dp[i]
    for i in range(1, N+1):
        for l, r in LR:
            dp[i] += s[min(i+l-1, N)] - s[max(i+r-1, 0)]
            dp[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()