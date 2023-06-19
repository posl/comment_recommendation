def dfs(cur, n, a, b, c, d, used, p):
    if cur == n:
        if p == list(range(1, n + 1)):
            return True
        else:
            return False
    for i in range(1, n + 1):
        if not used[i]:
            if a[cur] == c[i] and b[cur] == d[i]:
                used[i] = True
                if dfs(cur + 1, n, a, b, c, d, used, p):
                    return True
                used[i] = False
            elif a[cur] == d[i] and b[cur] == c[i]:
                used[i] = True
                if dfs(cur + 1, n, a, b, c, d, used, p):
                    return True
                used[i] = False
    return False
