def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, N + 1):
        for j in range(K):
            if i - L[j] >= 1:
                dp[i] += dp[i - L[j]]
            if i - R[j] >= 1:
                dp[i] -= dp[i - R[j] - 1]
    print(dp[N] % 998244353)

if __name__ == '__main__':
    main()