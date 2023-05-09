def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in range(N):
        ndp = [0] * (K + 1)
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k <= K:
                    ndp[j + k] += dp[j]
                    ndp[j + k] %= mod
        dp = ndp
    print(dp[K])
