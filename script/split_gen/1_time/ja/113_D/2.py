def solve():
    H,W,K = map(int,input().split())
    dp = [[0 for i in range(W)] for j in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            dp[i+1][j] += dp[i][j]*fib(j)*fib(W-j-1)
            dp[i+1][j] %= mod
            if j > 0:
                dp[i+1][j-1] += dp[i][j]*fib(j-1)*fib(W-j-1)
                dp[i+1][j-1] %= mod
            if j < W-1:
                dp[i+1][j+1] += dp[i][j]*fib(j)*fib(W-j-2)
                dp[i+1][j+1] %= mod
    print(dp[H][K-1])
