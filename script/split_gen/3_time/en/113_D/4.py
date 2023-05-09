def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for bit in range(1 << (W - 1)):
            if '11' in bin(bit):
                continue
            for w in range(W):
                if w > 0 and (bit >> (w - 1)) & 1:
                    dp[h + 1][w - 1] += dp[h][w]
                    dp[h + 1][w - 1] %= MOD
                elif w < W - 1 and (bit >> w) & 1:
                    dp[h + 1][w + 1] += dp[h][w]
                    dp[h + 1][w + 1] %= MOD
                else:
                    dp[h + 1][w] += dp[h][w]
                    dp[h + 1][w] %= MOD
    print(dp[H][K - 1])
