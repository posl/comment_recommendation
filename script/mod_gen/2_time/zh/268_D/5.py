def dfs(i, s, t):
    if i == n:
        if s in t:
            return -1
        else:
            return s
    for j in range(len(s) + 1):
        res = dfs(i + 1, s[:j] + a[i] + s[j:], t)
        if res != -1:
            return res
    return -1
n, m = map(int, input().split())
a = [input() for _ in range(n)]
t = [input() for _ in range(m)]
print(dfs(0, '', t))
