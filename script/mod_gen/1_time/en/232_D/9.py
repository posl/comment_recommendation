def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    # dp[i][j] = (i,j)にたどり着く方法の数
    dp = [[0] * W for i in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            if i != 0:
                dp[i][j] += dp[i-1][j]
            if j != 0:
                dp[i][j] += dp[i][j-1]
    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()