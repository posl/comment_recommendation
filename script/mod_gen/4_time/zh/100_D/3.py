def dfs(i, a, b, c):
    if i == n:
        return abs(a) + abs(b) + abs(c)
    else:
        return max(dfs(i + 1, a + x[i], b + y[i], c + z[i]),
                   dfs(i + 1, a + x[i], b + y[i], c - z[i]),
                   dfs(i + 1, a + x[i], b - y[i], c + z[i]),
                   dfs(i + 1, a + x[i], b - y[i], c - z[i]),
                   dfs(i + 1, a - x[i], b + y[i], c + z[i]),
                   dfs(i + 1, a - x[i], b + y[i], c - z[i]),
                   dfs(i + 1, a - x[i], b - y[i], c + z[i]),
                   dfs(i + 1, a - x[i], b - y[i], c - z[i]))
n, m = map(int, input().split())
x = []
y = []
z = []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append(a)
    y.append(b)
    z.append(c)
print(dfs(0, 0, 0, 0))
