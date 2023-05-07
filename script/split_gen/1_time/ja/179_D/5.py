def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: x[0])
    mod = 998244353
    dp = [0] * N
    dp[0] = 1
    s = 0
    for i in range(N):
        if i > 0:
            dp[i] = (dp[i] + s) % mod
        s = (s + dp[i]) % mod
        for l, r in LR:
            if i + l >= N:
                break
            dp[i + l] = (dp[i + l] + dp[i]) % mod
            if i + r + 1 < N:
                s = (s - dp[i + r + 1]) % mod
    print(dp[-1])
