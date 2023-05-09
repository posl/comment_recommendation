def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A[0], A[1]))
        return
    dp = [[0, 0] for _ in range(N)]
    dp[0][0] = A[0]
    dp[0][1] = -A[0]
    dp[1][0] = max(A[0] + A[1], A[0] - A[1])
    dp[1][1] = max(A[0] - A[1], A[0] + A[1])
    for i in range(2, N):
        dp[i][0] = max(dp[i-1][0] + A[i], dp[i-1][1] - A[i])
        dp[i][1] = max(dp[i-1][0] - A[i], dp[i-1][1] + A[i])
    print(max(dp[N-1][0], dp[N-1][1]))

if __name__ == '__main__':
    main()