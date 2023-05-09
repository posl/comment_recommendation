def dfs(v,p):
    for u in edges[v]:
        if u == p:
            continue
        cnt[u] += cnt[v]
        dfs(u,v)
N,Q = map(int,input().split())
edges = [[] for _ in range(N)]
cnt = [0]*N
for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
for _ in range(Q):
    p,x = map(int,input().split())
    cnt[p-1] += x
dfs(0,-1)
print(*cnt)

if __name__ == '__main__':
    dfs()