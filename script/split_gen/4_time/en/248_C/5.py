def main():
    N,M,K = map(int, input().split())
    mod = 998244353
    dp = [0]*(K+1)
    dp[0] = 1
    for i in range(1, N+1):
        new_dp = [0]*(K+1)
        for j in range(1, M+1):
            for k in range(K-i+1):
                new_dp[k+i] += dp[k]
                new_dp[k+i] %= mod
        dp = new_dp
    print(dp[K])
