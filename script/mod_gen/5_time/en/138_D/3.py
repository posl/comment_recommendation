def dfs(v,p):
    for u in to[v]:
        if u == p:
            continue
        counter[u] += counter[v]
        dfs(u,v)
n,q = map(int,input().split())
to = [[] for _ in range(n)]
counter = [0]*n
for _ in range(n-1):
    a,b = map(int,input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)
for _ in range(q):
    p,x = map(int,input().split())
    counter[p-1] += x
dfs(0,-1)
print(*counter)

if __name__ == '__main__':
    dfs()