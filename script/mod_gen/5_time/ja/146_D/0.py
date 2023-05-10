def dfs(v, p, c):
    color[c] += 1
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, c)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
color = [0] * N
dfs(0, -1, 0)
print(max(color))
for i in range(N-1):
    print(color[i+1])

if __name__ == '__main__':
    dfs()