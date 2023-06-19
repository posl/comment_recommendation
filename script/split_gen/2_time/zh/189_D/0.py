def dfs(i, x, s):
    if i == n:
        return s
    if s == 'AND':
        return dfs(i + 1, x, s) + dfs(i + 1, x + 1, s)
    else:
        return dfs(i + 1, x, s) * 2 + dfs(i + 1, x + 1, s)
n = int(input())
s = [input() for _ in range(n)]
print(dfs(0, 0, s[0]))
