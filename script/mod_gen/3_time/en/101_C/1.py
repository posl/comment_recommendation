def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = dp[i] + A[i]
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, dp[i + K] - dp[i])
    print(ans)

if __name__ == '__main__':
    main()