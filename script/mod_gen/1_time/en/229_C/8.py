def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for i in range(N)]
    cheese.sort()
    dp = [[0 for i in range(1001)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1001):
            if j < cheese[i-1][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cheese[i-1][0]]+cheese[i-1][0]*cheese[i-1][1])
    for i in range(1001):
        if dp[N][i] > W:
            print(i-1)
            return

if __name__ == '__main__':
    main()