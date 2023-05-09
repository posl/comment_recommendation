def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    
    # dp[i] = マスiにたどり着く方法の総数
    dp = [0] * (N+1)
    # dp[0] = 1
    dp[0] = 1
    # dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k] (i-k >= 0) + ... + dp[i-r] (i-r >= 0)
    # dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k] (i-k >= 0) + ... + dp[i-l] (i-l >= 0)
    for i in range(1, N+1):
        for j in range(K):
            l = i - L[j]
            r = i - R[j]
            if r < 0:
                r = 0
            if l < 0:
                l = 0
            dp[i] += dp[r] - dp[l-1]
        dp[i] = dp[i] % 998244353
    print(dp[N])

if __name__ == '__main__':
    main()