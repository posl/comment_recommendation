def dfs(h, w, a, b):
    if h < 0 or w < 0:
        return 0
    if h == 0 and w == 0:
        return 1
    if (h, w, a, b) in memo:
        return memo[(h, w, a, b)]
    res = 0
    if a:
        res += dfs(h-1, w, a-1, b) + dfs(h-2, w, a-1, b)
    if b:
        res += dfs(h, w-1, a, b-1) + dfs(h, w-2, a, b-1)
    memo[(h, w, a, b)] = res
    return res
H, W, A, B = map(int, input().split())
memo = {}
print(dfs(H, W, A, B))
