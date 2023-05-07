def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for i in range(N)]
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [float("inf")] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i - 1] + T[i])
        for j in A[i]:
            dp[i] = min(dp[i], dp[j - 1] + T[i])
    print(dp[-1])

if __name__ == '__main__':
    main()