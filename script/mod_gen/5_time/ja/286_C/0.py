def solve():
    N,A,B = map(int,input().split())
    S = input()
    dp = [[float('inf')]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i+1][0] = dp[i][0] + B
        dp[i+1][1] = min(dp[i][0],dp[i][1]) + A
        for j in range(2,i+2):
            if S[i-j+1] == S[i]:
                dp[i+1][j] = dp[i][j-2]
            else:
                dp[i+1][j] = min(dp[i][j-2],dp[i][j-1]) + A
    print(min(dp[N]))

if __name__ == '__main__':
    solve()