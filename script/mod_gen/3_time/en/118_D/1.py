def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i - A[j] >= 0 and dp[i - A[j]] != -1:
                dp[i] = max(dp[i], dp[i - A[j]] * 10 + A[j])
    print(dp[N])

if __name__ == '__main__':
    main()