def main():
    N, K = map(int, input().split())
    LRs = []
    for _ in range(K):
        LR = list(map(int, input().split()))
        LR.sort()
        LRs.append(LR)
    #print(LRs)
    #print(N, K)
    dp = [0] * (N+1)
    dp[1] = 1
    dpsum = [0] * (N+1)
    dpsum[1] = 1
    for i in range(2, N+1):
        for j in range(K):
            l = LRs[j][0]
            r = LRs[j][1]
            if i - r > 0:
                dp[i] += dpsum[i-l] - dpsum[i-r-1]
            elif i - l >= 0:
                dp[i] += dpsum[i-l]
        dp[i] %= 998244353
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= 998244353
    #print(dp)
    print(dp[N])
