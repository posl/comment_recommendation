def dfs(i, cost, level):
    if i == n:
        if level >= x:
            return cost
        else:
            return -1
    else:
        return min(dfs(i+1, cost + c[i], [level[j] + a[i][j] for j in range(m)]), dfs(i+1, cost, level))
n, m, x = map(int, input().split())
c = [0]*n
a = [[0]*m for _ in range(n)]
for i in range(n):
    c[i], *a[i] = map(int, input().split())
print(dfs(0, 0, [0]*m))
