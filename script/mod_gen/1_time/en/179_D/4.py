def solve():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            dp[i] += dp[max(0, i - R[j] - 1)] - dp[max(0, i - L[j] - 1)]
        dp[i] %= 998244353
    print(dp[N])
solve()

if __name__ == '__main__':
    solve()