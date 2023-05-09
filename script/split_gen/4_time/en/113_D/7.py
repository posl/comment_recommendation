def main():
    H, W, K = map(int, input().split())
    #print(H,W,K)
    if W == 1:
        print(1)
        exit()
    dp = [[0 for _ in range(W)] for _ in range(H+1)]
    dp[0][0] = 1
    for h in range(1, H+1):
        for w in range(W):
            dp[h][w] += dp[h-1][w] * (w != 0 and w != W-1)
            dp[h][w] += dp[h-1][w-1] * (w != 0)
            dp[h][w] += dp[h-1][w+1] * (w != W-1)
            dp[h][w] %= 10**9 + 7
    print(dp[H][K-1])
