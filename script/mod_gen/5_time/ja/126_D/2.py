def dfs(s, c):
    color[s] = c
    for i in range(len(G[s])):
        if color[G[s][i]] == 0:
            dfs(G[s][i], -c)
N = int(input())
G = [[] for i in range(N)]
color = [0] * N
for i in range(N - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)
dfs(0, 1)
for i in range(N):
    if color[i] == 1:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    dfs()