def dfs(n, m, l):
    if n == 0:
        print(*l)
        return
    if len(l) == 0:
        for i in range(1, m + 1):
            dfs(n - 1, m, l + [i])
    else:
        for i in range(l[-1], m + 1):
            dfs(n - 1, m, l + [i])
n, m = map(int, input().split())
dfs(n, m, [])
