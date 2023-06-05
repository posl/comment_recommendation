def dfs(v, p, c):
    global color
    color[c] = True
    result[v] = c
    for w in g[v]:
        if w == p:
            continue
        nc = 1
        while color[nc]:
            nc += 1
        dfs(w, v, nc)
n = int(input())
g = [[] for _ in range(n+1)]
color = [False] * (n+1)
result = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
dfs(1, -1, 1)
print(max(result))
for i in range(1, n):
    print(result[i])

if __name__ == '__main__':
    dfs()