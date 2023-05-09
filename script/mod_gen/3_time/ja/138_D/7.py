def dfs(v, p, d):
    for i in G[v]:
        if i != p:
            D[i] += d
            dfs(i, v, D[i])
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
D = [0] * N
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
for i in range(Q):
    p, x = map(int, input().split())
    D[p-1] += x
dfs(0, -1, 0)
print(*D)

if __name__ == '__main__':
    dfs()