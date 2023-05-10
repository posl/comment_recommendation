def dfs(n, m, a):
    if len(a) == n:
        print(" ".join(map(str, a)))
        return
    s = a[-1] if a else 1
    for i in range(s, m + 1):
        dfs(n, m, a + [i])
n, m = map(int, input().split())
dfs(n, m, [])
