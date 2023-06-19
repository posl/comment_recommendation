def dfs(G, v, c):
    color[v] = c
    for i in G[v]:
        if color[i] == 0:
            dfs(G, i, c)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
color = [0]*N
color[0] = 1
for i in G[0]:
    color[i] = 2
for i in G[0]:
    dfs(G, i, color[i])
print(max(color))
for i in range(N-1):
    print(color[i+1])

if __name__ == '__main__':
    dfs()