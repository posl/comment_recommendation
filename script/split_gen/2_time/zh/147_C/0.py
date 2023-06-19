def dfs(i, n, a, x, y):
    if i == n:
        return 0
    else:
        ans = 0
        for j in range(a[i]):
            if y[i][j] == 1:
                ans = max(ans, dfs(i+1, n, a, x, y)+1)
            else:
                ans = max(ans, dfs(i+1, n, a, x, y))
        return ans
n = int(input())
a = []
x = []
y = []
for i in range(n):
    a.append(int(input()))
    x.append([])
    y.append([])
    for j in range(a[i]):
        x[i].append(0)
        y[i].append(0)
        x[i][j], y[i][j] = map(int, input().split())
print(dfs(0, n, a, x, y))
