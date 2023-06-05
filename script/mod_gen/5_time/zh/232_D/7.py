def main():
    #input
    h, w = map(int, input().split())
    maze = [list(input()) for i in range(h)]
    #init
    dp = [[0 for j in range(w)] for i in range(h)]
    dp[0][0] = 1
    #loop
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % 1000000007
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % 1000000007
    #output
    print(dp[h-1][w-1])

if __name__ == '__main__':
    main()