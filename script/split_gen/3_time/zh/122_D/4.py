def main():
    n = int(input())
    mod = 10**9+7
    dp = [0]*64
    # 0:A,1:C,2:G,3:T
    for i in range(64):
        if i & 1 and i >> 1 & 1 and i >> 2 & 1:
            continue
        if i & 1 and i >> 1 & 1 and i >> 3 & 1:
            continue
        if i & 1 and i >> 2 & 1 and i >> 3 & 1:
            continue
        if i >> 1 & 1 and i >> 2 & 1 and i >> 3 & 1:
            continue
        dp[i] = 1
    for i in range(4,n+1):
        ndp = [0]*64
        for j in range(64):
            for k in range(4):
                nj = (j << 1 | k) & 63
                if nj & 1 and nj >> 1 & 1 and nj >> 2 & 1:
                    continue
                if nj & 1 and nj >> 1 & 1 and nj >> 3 & 1:
                    continue
                if nj & 1 and nj >> 2 & 1 and nj >> 3 & 1:
                    continue
                if nj >> 1 & 1 and nj >> 2 & 1 and nj >> 3 & 1:
                    continue
                ndp[nj] += dp[j]
                ndp[nj] %= mod
        dp = ndp
    print(sum(dp) % mod)
