def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    dp = [[float('inf')]*(X+Y+1) for i in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X+Y+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j >= A[i][0]:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-A[i][0]]+1)
            if j >= A[i][1]:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-A[i][1]]+1)
    ans = float('inf')
    for i in range(X, X+Y+1):
        ans = min(ans, dp[N][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()