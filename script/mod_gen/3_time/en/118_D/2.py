def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for j in range(M):
            if i + A[j] <= N:
                dp[i + A[j]] = max(dp[i + A[j]], dp[i] * 10 + A[j])
    print(dp[N])

if __name__ == '__main__':
    main()