def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        for j in range(K):
            if i - A[j] >= 0:
                dp[i] = max(dp[i], dp[i - A[j]] + 1)
    print(N - dp[N])

if __name__ == '__main__':
    main()