def dfs(n,m,a):
    if len(a) == n:
        print(a)
        return
    s = 1
    if len(a) > 0:
        s = a[-1] + 1
    for i in range(s, m + 1):
        a.append(i)
        dfs(n, m, a)
        a.pop()
