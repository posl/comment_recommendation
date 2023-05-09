def main():
    N = int(input())
    A = list(map(int, input().split()))
    INF = 10**5+5
    dp = [[INF for _ in range(3)] for _ in range(N+1)]
    dp[0][0] = 0
    dp[0][1] = 1
    dp[0][2] = 2
    for i in range(N):
        dp[i+1][0] = min(dp[i][0], dp[i][1], dp[i][2]) + (A[i] != A[N-i-1])
        dp[i+1][1] = min(dp[i][0]+1, dp[i][1], dp[i][2]) + (A[i] != A[N-i-1])
        dp[i+1][2] = min(dp[i][0]+2, dp[i][1]+1, dp[i][2]) + (A[i] != A[N-i-1])
    print(min(dp[N][0], dp[N][1], dp[N][2]))

if __name__ == '__main__':
    main()