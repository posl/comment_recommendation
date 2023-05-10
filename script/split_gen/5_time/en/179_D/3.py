def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * N
    dp[0] = 1
    dpsum = [0] * N
    dpsum[0] = 1
    for i in range(1, N):
        for j in range(K):
            if i - L[j] >= 0:
                dp[i] += dpsum[i - L[j]]
                dp[i] %= 998244353
            if i - R[j] - 1 >= 0:
                dp[i] -= dpsum[i - R[j] - 1]
                dp[i] %= 998244353
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= 998244353
    print(dp[N - 1])
