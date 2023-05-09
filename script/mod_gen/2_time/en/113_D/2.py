def main():
    H, W, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*W for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j+1]) % mod
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
            elif j == W-1:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j-1]) % mod
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
            else:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j-1]) % mod
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
                dp[i+1][j] = (dp[i+1][j] + dp[i][j+1]) % mod
    print(dp[H][K-1])
main()
I used the same method as the previous problem, but I made a mistake when I wrote the code. I wrote the following code:
dp[i+1][j] = (dp[i+1][j] + dp[i][j-1]) % mod
dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
dp[i+1][j] = (dp[i+1][j] + dp[i][j+1]) % mod
However, this code is wrong. The correct code is as follows:
dp[i+1][j] += (dp[i][j-1] + dp[i][j] + dp[i][j+1]) % mod
I made a mistake because I didn’t understand the meaning of the += operator. I should have written the following code:
dp[i+1][j] = (dp[i+1][j] + (dp[i][j-1] + dp[i][j] + dp[i][j+1

if __name__ == '__main__':
    main()