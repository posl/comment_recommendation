def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    num = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1 for i in range(N + 1)]
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for j in range(M):
            dp[i + num[A[j] - 1]] = max(dp[i + num[A[j] - 1]], dp[i] * 10 + A[j])
    print(dp[N])

if __name__ == '__main__':
    main()