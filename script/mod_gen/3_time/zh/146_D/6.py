def dfs(v, p=-1):
    global color, G
    c = 1
    for u in G[v]:
        if u == p:
            continue
        if c == color[v]:
            c += 1
        color[u] = c
        dfs(u, v)
        c += 1
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
color = [0] * N
color[0] = 1
dfs(0)
print(max(color))
for c in color:
    print(c)

if __name__ == '__main__':
    dfs()