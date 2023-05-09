def solve():
    H, W, K = map(int, input().split())
    MOD = 10**9+7
    dp = [[0]*W for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            for k in range(1<<(W-1)):
                ok = True
                for l in range(W-2):
                    if (k>>l)&1 and (k>>(l+1))&1:
                        ok = False
                if not ok:
                    continue
                nj = j
                if (k>>j)&1:
                    nj += 1
                elif j > 0 and (k>>(j-1))&1:
                    nj -= 1
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= MOD
    print(dp[H][K-1])
