def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    #print(H, W, C)
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1 if C[0][0] == "." else 0
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == "#":
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #print(dp)
    print(dp[H-1][W-1] % (10**9+7))
