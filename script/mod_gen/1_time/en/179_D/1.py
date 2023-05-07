def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    #dp[i] = i番目までのセルに到達する方法の総数
    dp = [0] * (N + 1)
    dp[1] = 1
    #dp[i] = dp[i-1] + ... + dp[i-k]
    #dp[i] = dp[i-1] - dp[i-k-1] + dp[i]
    #dp[i] = 2*dp[i-1] - dp[i-k-1]
    dp2 = [0] * (N + 1)
    dp2[1] = 1
    for i in range(2, N + 1):
        dp[i] = (2 * dp[i - 1]) % 998244353
        for j in range(K):
            if i - L[j] > 0:
                dp[i] = (dp[i] - dp2[i - L[j]] + 998244353) % 998244353
        dp2[i] = (dp2[i - 1] + dp[i]) % 998244353
    print(dp[N])

if __name__ == '__main__':
    main()