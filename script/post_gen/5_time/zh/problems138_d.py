Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(now,par):
    for i in range(len(tree[now])):
        if tree[now][i] != par:
            dfs(tree[now][i],now)
            count[now] += count[tree[now][i]]
    return

N,Q = map(int,input().split())
tree = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
count = [0]*N
for i in range(Q):
    p,x = map(int,input().split())
    count[p-1] += x
dfs(0,-1)
for i in count:
    print(i,end=" ")
print()

=======
Suggestion 2

def dfs(u,p):
    for v in g[u]:
        if v==p:continue
        cnt[v]+=cnt[u]
        dfs(v,u)

n,q=map(int,input().split())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
cnt=[0]*(n+1)
for _ in range(q):
    p,x=map(int,input().split())
    cnt[p]+=x
dfs(1,-1)
print(*cnt[1:])

=======
Suggestion 3

def main():
    n,q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    px = [list(map(int, input().split())) for _ in range(q)]

    #print("n,q:",n,q)
    #print("ab:",ab)
    #print("px:",px)

    #构建树，用邻接表表示
    #根据ab构建邻接表
    adj = [[] for _ in range(n+1)]
    for i in range(n-1):
        a,b = ab[i]
        adj[a].append(b)
        adj[b].append(a)
    #print("adj:",adj)

    #构建树，用邻接表表示
    #根据ab构建邻接表
    adj = [[] for _ in range(n+1)]
    for i in range(n-1):
        a,b = ab[i]
        adj[a].append(b)
        adj[b].append(a)
    #print("adj:",adj)

    #计算每个节点的子节点数
    #计算每个节点的子节点数
    #print("adj:",adj)
    #print("px:",px)
    #print("n,q:",n,q)
    #print("ab:",ab)
    #print("px:",px)

    #构建树，用邻接表表示
    #根据ab构建邻接表
    adj = [[] for _ in range(n+1)]
    for i in range(n-1):
        a,b = ab[i]
        adj[a].append(b)
        adj[b].append(a)
    #print("adj:",adj)

    #计算每个节点的子节点数
    def dfs(x,par):
        for y in adj[x]:
            if y == par:
                continue
            dfs(y,x)
            c[x] += c[y]

    c = [0]*(n+1)
    for i in range(q):
        p,x = px[i]
        c[p] += x
    #print("c:",c)
    dfs(1,0)
    print(" ".join(map(str,c[1:])))

=======
Suggestion 4

def dfs(v, p, d):
    global c
    global ans
    c[v] += d
    ans[v-1] += c[v]
    for i in range(len(g[v])):
        if g[v][i] != p:
            dfs(g[v][i], v, d)

n, q = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

c = [0] * (n+1)
ans = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    dfs(p, -1, x)

print(*ans)

=======
Suggestion 5

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

=======
Suggestion 6

def main():
    global N, Q, a, b, p, x, tree, ans
    N, Q = map(int, input().split())
    a = [0]*N
    b = [0]*N
    p = [0]*Q
    x = [0]*Q
    tree = [[] for i in range(N)]
    ans = [0]*N
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
        tree[a[i]].append(b[i])
        tree[b[i]].append(a[i])
    for i in range(Q):
        p[i], x[i] = map(int, input().split())
        p[i] -= 1
    dfs(0, -1)
    print(" ".join(map(str, ans)))

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def dfs(u, p):
    for v in G[u]:
        if v == p:
            continue
        C[v] += C[u]
        dfs(v, u)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
C = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    C[p - 1] += x
dfs(0, -1)
print(*C)

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    links = []
    for _ in range(n - 1):
        links.append(list(map(int, input().split())))
    operations = []
    for _ in range(q):
        operations.append(list(map(int, input().split())))

    tree = []
    for _ in range(n):
        tree.append(0)

    for operation in operations:
        tree[operation[0] - 1] += operation[1]

    for link in links:
        if link[0] == 1:
            tree[link[1] - 1] += tree[0]
        else:
            tree[link[1] - 1] += tree[link[0] - 1]

    print(' '.join(map(str, tree)))

=======
Suggestion 10

def dfs(v, p, x):
    global ans
    ans[v] += x
    for i in G[v]:
        if i != p:
            dfs(i, v, x)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

ans = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    dfs(p-1, -1, x)

print(*ans)
