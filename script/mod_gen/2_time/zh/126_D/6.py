def dfs(u,color):
    global G
    global visited
    global ans
    global color
    visited[u] = True
    color[u] = c
    for v in G[u]:
        if visited[v]:
            continue
        dfs(v,1-c)
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
visited = [False]*N
color = [0]*N
ans = []
dfs(0,0)
for i in range(N):
    print(color[i])

if __name__ == '__main__':
    dfs()