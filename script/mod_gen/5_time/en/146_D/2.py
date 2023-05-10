def dfs(v, p):
    global c
    color = 1
    for u in G[v]:
        if u == p:
            continue
        if color == c[v]:
            color += 1
        c[u] = color
        color += 1
        dfs(u, v)
N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
c = [0] * (N+1)
c[1] = 1
dfs(1, -1)
print(max(c))
for i in range(1, N):
    print(c[i+1])

if __name__ == '__main__':
    dfs()