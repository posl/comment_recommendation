def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    dp = [[0] * 5 for _ in range(N)]
    for i in range(N):
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j == A[i][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + A[i][2])
            elif j - 1 == A[i][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + A[i][2])
            elif j + 1 == A[i][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j+1] + A[i][2])
    print(max(dp[N-1]))

if __name__ == '__main__':
    main()