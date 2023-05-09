def main():
    N, K = map(int, input().split())
    S = []
    for _ in range(K):
        S.append(list(map(int, input().split())))
    MOD = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(1, N):
        for j in range(K):
            l, r = S[j]
            dp[i + l] += dp[i]
            dp[i + l] %= MOD
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= MOD
    print(dp[N])
