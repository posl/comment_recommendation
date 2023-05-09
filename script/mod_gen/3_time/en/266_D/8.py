def main():
    #input
    N = int(input())
    XTs = [[*map(int, input().split())] for _ in range(N)]
    XTs.sort(key=lambda x: x[0])
    XTs = [[0,0,0]] + XTs
    #solve
    dp = [[[0]*5 for _ in range(5)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(5):
            for k in range(5):
                t, x, a = XTs[i]
                if j == k:
                    if t == XTs[i-1][0] + abs(j-x):
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-1][k-1] + a)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
                else:
                    if t == XTs[i-1][0] + abs(j-x):
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-1][k] + a)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
    #output
    print(max(dp[N][0][0], dp[N][0][1], dp[N][0][2], dp[N][0][3], dp[N][0][4]))

if __name__ == '__main__':
    main()