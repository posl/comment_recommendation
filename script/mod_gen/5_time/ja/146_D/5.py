def dfs(v, p=-1, c=-1):
    global ans
    c += 1
    color = 0
    for u in G[v]:
        if u == p:
            continue
        color += 1
        if c == color:
            color += 1
        ans[u] = color
        dfs(u, v, color)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [0]*N
dfs(0)
print(max(ans))
for a in ans:
    print(a)

if __name__ == '__main__':
    dfs()