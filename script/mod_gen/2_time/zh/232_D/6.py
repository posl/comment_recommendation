def dfs(h, w):
    if h == H - 1 and w == W - 1:
        return 1
    if memo[h][w] != -1:
        return memo[h][w]
    res = 0
    for i in range(2):
        nh = h + dh[i]
        nw = w + dw[i]
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if S[nh][nw] == '#':
            continue
        res += dfs(nh, nw)
    memo[h][w] = res
    return res
H, W = map(int, input().split())
S = [input() for _ in range(H)]
memo = [[-1] * W for _ in range(H)]
dh = [0, 1]
dw = [1, 0]
print(dfs(0, 0))
