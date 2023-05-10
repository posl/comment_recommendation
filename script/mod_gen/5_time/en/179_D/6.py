def main():
    N, K = map(int, input().split())
    LRs = []
    for _ in range(K):
        LR = list(map(int, input().split()))
        LRs.append(LR)
    #print(N, K)
    #print(LRs)
    #dp[i]: i番目のセルにたどり着く方法の総数
    dp = [0] * N
    dp[0] = 1
    #dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-L] (i-L >= 0)
    for i in range(1, N):
        for LR in LRs:
            L = LR[0]
            R = LR[1]
            if i - L >= 0:
                dp[i] += dp[i-L]
                dp[i] %= 998244353
            if i - R - 1 >= 0:
                dp[i] -= dp[i-R-1]
                dp[i] %= 998244353
    #print(dp)
    ans = dp[N-1]
    print(ans)

if __name__ == '__main__':
    main()