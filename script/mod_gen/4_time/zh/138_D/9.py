def dfs(x):
    global cnt
    cnt[x] += cnt[par[x]]
    for y in G[x]:
        if y != par[x]:
            dfs(y)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
par = [0]*N
cnt = [0]*N
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
for i in range(Q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x
dfs(0)
print(*cnt)

if __name__ == '__main__':
    dfs()