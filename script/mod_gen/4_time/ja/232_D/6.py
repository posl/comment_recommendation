def main():
    H,W = map(int,input().split())
    C = [input() for _ in range(H)]
    #print(H,W,C)
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == '#':
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #print(dp)
    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()