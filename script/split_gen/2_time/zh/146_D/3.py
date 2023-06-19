def dfs(v, p, c):
    global color, G
    color[v] = c
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        dfs(G[v][i], v, (c+1)%len(G[v]))
n = int(input())
G = [[] for i in range(n)]
color = [0]*n
for i in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
dfs(0, -1, 0)
print(max(color)+1)
for i in range(n-1):
    print(color[i]+1)
