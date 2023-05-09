def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort()
    mod = 998244353
    def solve(N, LR):
        dp = [0] * (N + 1)
        dp[1] = 1
        for i in range(1, N):
            for l, r in LR:
                dp[i + l] = (dp[i + l] + dp[i]) % mod
                dp[i + r + 1] = (dp[i + r + 1] - dp[i]) % mod
        return dp[N]
    print(solve(N, LR))
