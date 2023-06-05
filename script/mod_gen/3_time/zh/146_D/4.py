def dfs(v, p, c):
    global color
    global G
    color[c] += 1
    k = 1
    for i in G[v]:
        if i == p:
            continue
        if k == c:
            k += 1
        dfs(i, v, k)
        k += 1
N = int(input())
color = [0]*(N+1)
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
dfs(1, -1, 1)
print(max(color))
for i in range(N-1):
    print(color[i+1])

if __name__ == '__main__':
    dfs()