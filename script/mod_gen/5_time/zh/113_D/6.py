def dfs(h,w,k):
    if dp[h][w][k] >= 0:
        return dp[h][w][k]
    if w == 0:
        return 1 if k == 0 else 0
    res = 0
    for i in range(1 << (w-1)):
        ok = True
        for j in range(w-2):
            if (i >> j) & 1 and (i >> (j+1)) & 1:
                ok = False
        if not ok:
            continue
        for j in range(w):
            if (i >> j) & 1:
                dfs(h-1,w-j-1,k-1)
            else:
                dfs(h-1,w-j-1,k)
        res += dfs(h-1,w,k)
        res %= mod
    dp[h][w][k] = res
    return res
mod = 1000000007
h,w,k = map(int,input().split())
dp = [[[-1] * (w+1) for _ in range(h+1)] for _ in range(4)]
print(dfs(h,w,k))
