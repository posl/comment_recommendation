def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[]] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = T[0]
    for i in range(N-1):
        dp[i+1] = min(dp[i+1], dp[i] + T[i+1])
        for j in range(K[i]):
            dp[A[i][j] - 1] = min(dp[A[i][j] - 1], dp[i] + T[A[i][j] - 1])
    print(dp[N-1])

if __name__ == '__main__':
    main()