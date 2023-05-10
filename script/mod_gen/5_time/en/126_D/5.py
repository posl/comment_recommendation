def dfs(v, p, d):
    for i in G[v]:
        if i == p:
            continue
        if d % 2 == 0:
            color[i] = 0
        else:
            color[i] = 1
        dfs(i, v, d + 1)
N = int(input())
G = [[] for i in range(N)]
color = [0] * N
for i in range(N - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)
color[0] = 0
dfs(0, -1, 0)
for i in color:
    print(i)

if __name__ == '__main__':
    dfs()