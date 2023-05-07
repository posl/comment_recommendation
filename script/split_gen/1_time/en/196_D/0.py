def solve(H, W, A, B):
    dp = [[[0 for _ in range(2)] for _ in range(W+1)] for _ in range(H+1)]
    dp[0][0][0] = 1
    for h in range(H):
        for w in range(W):
            for k in range(2):
                if h >= A and w >= B:
                    dp[h][w][k] += dp[h-A][w-B][k]
                if h >= B and w >= A:
                    dp[h][w][k] += dp[h-B][w-A][k]
                if k == 0:
                    dp[h][w][k] += dp[h][w][1]
                dp[h][w+1][k] += dp[h][w][k]
                dp[h+1][w][k] += dp[h][w][k]
    return dp[H][W][0]
H, W, A, B = map(int, input().split())
print(solve(H, W, A, B))
