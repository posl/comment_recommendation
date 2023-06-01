Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v,p):
    for u in edge[v]:
        if u==p:
            continue
        cnt[u]+=cnt[v]
        dfs(u,v)

n,q=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
cnt=[0]*n
for _ in range(q):
    p,x=map(int,input().split())
    cnt[p-1]+=x
dfs(0,-1)
print(*cnt)

=======
Suggestion 2

def dfs(now, pre):
    for next in edges[now]:
        if next == pre:
            continue
        counter[next] += counter[now]
        dfs(next, now)

N, Q = map(int, input().split())
edges = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

counter = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x

dfs(0, -1)
print(*counter)

=======
Suggestion 3

def dfs(v, p):
    global ans
    ans[v] += ans[p]
    for u in edge[v]:
        if u == p:
            continue
        dfs(u, v)

n, q = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
ans = [0] * (n + 1)
for _ in range(q):
    p, x = map(int, input().split())
    ans[p] += x
dfs(1, 0)
print(*ans[1:])

=======
Suggestion 4

def dfs(u,p):
    global cnt
    cnt[u]+=cnt[p]
    for v in G[u]:
        if v==p:continue
        dfs(v,u)

N,Q = map(int,input().split())
G = [[] for i in range(N)]
cnt = [0]*N
for i in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
for i in range(Q):
    p,x = map(int,input().split())
    p-=1
    cnt[p]+=x
dfs(0,-1)
print(*cnt)

=======
Suggestion 5

def dfs(u):
    seen[u] = True
    res[u] += add[u]
    for v in adj[u]:
        if not seen[v]:
            add[v] += add[u]
            dfs(v)

n, q = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

res = [0] * (n+1)
add = [0] * (n+1)
seen = [False] * (n+1)
for _ in range(q):
    p, x = map(int, input().split())
    add[p] += x

dfs(1)
print(*res[1:])

=======
Suggestion 6

def main():
    N,Q = map(int, input().split())
    A = [0]*(N+1)
    for i in range(N-1):
        a,b = map(int, input().split())
        A[a] += 1
        A[b] += 1
    for i in range(Q):
        p,x = map(int, input().split())
        A[p] += x
    print(' '.join(map(str, A[1:])))

=======
Suggestion 7

def dfs(v,p):
    for u in g[v]:
        if u==p: continue
        cnt[u]+=cnt[v]
        dfs(u,v)

n,q=map(int,input().split())
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
cnt=[0]*n
for i in range(q):
    p,x=map(int,input().split())
    cnt[p-1]+=x
dfs(0,-1)
print(*cnt)

=======
Suggestion 8

def f(n,q,ab,pjxj):
    #print(n,q,ab,pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)

    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)

    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)

    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)

    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)

    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)

    #print("ab",ab)
    #print("pjxj",pjxj)
    #print("ab",ab)
    #print("pjxj",pjxj)

    #print("ab",ab)
    #print("pjxj",pjxj)

    #print("ab",

=======
Suggestion 9

def dfs(v, p, d):
    depth[v] = d
    for i in range(len(G[v])):
        if G[v][i] != p:
            dfs(G[v][i], v, d+1)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

depth = [0] * N
dfs(0, -1, 0)

ans = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x

for i in range(N):
    print(ans[i], end=' ')
print()

for i in range(N):
    print(ans[i], end=' ')
print()

=======
Suggestion 10

def main():
    pass
