def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in A[i]:
            dp[i] = max(dp[i], dp[j] + T[j])
        dp[i] += T[i]
    print(dp[N])

if __name__ == '__main__':
    main()