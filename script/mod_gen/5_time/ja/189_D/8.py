def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(N):
        if S[i] == "AND":
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0] + dp[i][1]*2
        else:
            dp[i+1][0] = dp[i][0]*2 + dp[i][1]
            dp[i+1][1] = dp[i][1]
    print(dp[N][1])

if __name__ == '__main__':
    solve()