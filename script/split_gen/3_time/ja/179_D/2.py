def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for _ in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N + 1):
        for j in range(K):
            if i + L[j] <= N:
                dp[i + L[j]] += dp[i]
                dp[i + L[j]] %= 998244353
            if i + R[j] + 1 <= N:
                dp[i + R[j] + 1] -= dp[i]
                dp[i + R[j] + 1] %= 998244353
    print(dp[N])
