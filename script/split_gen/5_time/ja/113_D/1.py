def solve():
    H, W, K = map(int, input().split())
    dp = [[0 for _ in range(W)] for _ in range(H+1)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            for k in range(1 << (W-1)):
                # 横線が引けない条件
                if ((k >> (W-2)) & 1) and ((k >> (W-3)) & 1):
                    continue
                # 横線が引けない条件
                if ((k >> (W-2)) & 1) and (w < W-2):
                    continue
                # 横線が引けない条件
                if ((k >> (W-3)) & 1) and (w > 0):
                    continue
                dp[h+1][w] += dp[h][w-1] if w > 0 else 0
                dp[h+1][w] += dp[h][w+1] if w < W-1 else 0
                dp[h+1][w] %= 1000000007
    print(dp[H][K-1])
