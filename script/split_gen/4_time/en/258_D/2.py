def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    def check(t):
        dp = [float('inf')] * (N + 1)
        dp[0] = 0
        for i in range(N):
            dp[i + 1] = min(dp[i + 1], dp[i] + A[i])
            dp[i + 1] = min(dp[i + 1], dp[max(0, i - X + 1)] + B[max(0, i - X + 1)])
        return dp[N] <= t
    ok = 10**18
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
