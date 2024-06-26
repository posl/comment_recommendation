def dfs(v,p):
    for u in G[v]:
        if u != p:
            C[u] += C[v]
            dfs(u,v)
N,Q = map(int,input().split())
G = [[] for i in range(N)]
C = [0]*N
for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
for i in range(Q):
    p,x = map(int,input().split())
    C[p-1] += x
dfs(0,-1)
print(*C)

if __name__ == '__main__':
    dfs()