def dfs(i, g, v, d):
    v[i] = True
    for j in g[i]:
        if v[j] == False:
            d[j] = d[i] + 1
            dfs(j, g, v, d)
n = int(input())
a = list(map(int, input().split()))
g = [[] for i in range(2*n+1)]
for i in range(n):
    g[a[i]].append(i+1)
    g[a[i]+1].append(i+1)
v = [False]*(2*n+1)
d = [0]*(2*n+1)
dfs(1, g, v, d)
for i in range(1, 2*n+1):
    print(d[i])
