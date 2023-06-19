def dfs(v):
    global color
    global flag
    color[v] = 1
    for i in range(len(edge[v])):
        if color[edge[v][i]] == 0:
            dfs(edge[v][i])
        elif color[edge[v][i]] == 2:
            flag = False
    color[v] = 2
n,m = map(int,input().split())
edge = [[] for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
color = [0]*n
ans = 0
for i in range(n):
    if color[i] == 0:
        flag = True
        dfs(i)
        if flag:
            ans += 1
print(ans)
