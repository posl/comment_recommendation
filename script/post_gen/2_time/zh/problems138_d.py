Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def tree_add(tree, v, x):
    tree[v] += x
    for i in range(1, len(tree)):
        if tree[i] == v:
            tree_add(tree, i, x)
    return tree

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        E[a-1].append(b-1)
        E[b-1].append(a-1)
    P = [0]*N
    for _ in range(Q):
        p, x = map(int, input().split())
        P[p-1] += x
    ans = [0]*N
    def dfs(v, p):
        ans[v] = P[v]
        for nv in E[v]:
            if nv == p:
                continue
            P[nv] += P[v]
            dfs(nv, v)
    dfs(0, -1)
    print(*ans)

=======
Suggestion 3

def main():
    n,q = map(int,input().split())
    a = [0 for _ in range(n)]
    for _ in range(n-1):
        i,j = map(int,input().split())
        a[i-1] += 1
        a[j-1] += 1
    for _ in range(q):
        p,x = map(int,input().split())
        a[p-1] += x
    print(*a)

=======
Suggestion 4

def main():
    n,q = map(int,input().split())
    ab = [list(map(int,input().split())) for i in range(n-1)]
    px = [list(map(int,input().split())) for i in range(q)]

    #print(n,q,ab,px)
    #print()

    #print(parent)
    #print()
    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)
    #print()

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)
    #print()

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)
    #print()

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)
    #print()

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)
    #print()

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)
    #print()

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)
    #print()

    #print(ans)
    #print()
    #print(visited)
    #print()
    #print(visited2)
    #print()
    #print()

    ans = [0 for i in range(n)]
    visited = [0 for i in range(n)]
    visited2 = [0 for

=======
Suggestion 5

def dfs(x):
    for i in range(len(tree[x])):
        dfs(tree[x][i])
        c[x] += c[tree[x][i]]

n,q = map(int,input().split())
tree = [[] for _ in range(n)]
c = [0]*n
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
for i in range(q):
    p,x = map(int,input().split())
    c[p-1] += x
dfs(0)
print(*c)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def dfs(x):
    for i in range(len(g[x])):
        if i == 0:
            continue
        dfs(g[x][i])
        cnt[x] += cnt[g[x][i]]
    return

n, q = map(int, input().split())
g = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
for _ in range(q):
    p, x = map(int, input().split())
    cnt[p] += x
dfs(1)
print(*cnt[1:])

=======
Suggestion 8

def dfs(v):
    global cnt
    cnt[v] += cnt[v-1]
    for i in range(len(g[v])):
        dfs(g[v][i])

n, q = map(int, input().split())
g = [[] for i in range(n+1)]
cnt = [0 for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)

for i in range(q):
    p, x = map(int, input().split())
    cnt[p] += x

dfs(1)

for i in cnt[1:]:
    print(i, end=' ')
print()
