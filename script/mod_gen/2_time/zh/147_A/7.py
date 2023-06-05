def dfs(v, p, c):
    global color
    color[c] += 1
    for e in G[v]:
        if e == p:
            continue
        dfs(e, v, c)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
color = [0] * N
dfs(0, -1, 0)
print(max(color))
for i in range(N - 1):
    print(color[i + 1])

if __name__ == '__main__':
    dfs()