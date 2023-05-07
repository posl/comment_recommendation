def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, N+1):
        for l, r in LR:
            dp[i] += dp[i-l] - dp[i-r-1]
    print(dp[N] % 998244353)
