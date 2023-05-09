def main():
    h,w,k = map(int,input().split())
    if k == 1:
        print(2**(w-1) % 1000000007)
    elif k == w:
        print(2**(w-2) % 1000000007)
    else:
        dp = [[0]*w for _ in range(h+1)]
        dp[0][0] = 1
        for i in range(h):
            for j in range(w):
                if j == 0:
                    dp[i+1][j] = dp[i][j]*2 + dp[i][j+1]
                elif j == w-1:
                    dp[i+1][j] = dp[i][j]*2 + dp[i][j-1]
                else:
                    dp[i+1][j] = dp[i][j]*2 + dp[i][j+1] + dp[i][j-1]
        print(dp[h][k-1] % 1000000007)
