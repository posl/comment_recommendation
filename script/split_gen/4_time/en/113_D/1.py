def main():
    H, W, K = map(int, input().split())
    dp = [0] * (W + 1)
    dp[0] = 1
    mod = 10 ** 9 + 7
    for i in range(H):
        ndp = [0] * (W + 1)
        for j in range(W):
            for k in range(2 ** (W - 1)):
                ok = True
                for l in range(W - 2):
                    if (k >> l) & 1 and (k >> (l + 1)) & 1:
                        ok = False
                if ok:
                    if j >= 1 and (k >> (j - 1)) & 1:
                        ndp[j - 1] += dp[j]
                        ndp[j - 1] %= mod
                    elif j <= W - 2 and (k >> j) & 1:
                        ndp[j + 1] += dp[j]
                        ndp[j + 1] %= mod
                    else:
                        ndp[j] += dp[j]
                        ndp[j] %= mod
        dp = ndp
    print(dp[K - 1])
