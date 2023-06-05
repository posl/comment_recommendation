def dfs(i, n, a, b):
    if i == n:
        return b
    if i == 0:
        return max(dfs(i+1, n, a, b), dfs(i+1, n, a, b^a[i][1]))
    else:
        return max(dfs(i+1, n, a, b), dfs(i+1, n, a, b^a[i][1]), dfs(i+1, n, a, b^a[i][0]))
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = 0
print(dfs(0, n, a, b))
