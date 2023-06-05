def dfs(v, p, c):
    color[c] = True
    col[v] = c
    for u in G[v]:
        if u == p:
            continue
        c += 1
        while color[c]:
            c += 1
        dfs(u, v, c)
        c -= 1
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
col = [0] * N
color = [False] * N
dfs(0, -1, 0)
print(max(col))
for i in range(N - 1):
    print(col[i] + 1)

if __name__ == '__main__':
    dfs()