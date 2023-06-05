Synthesizing 10/10 solutions

=======
Suggestion 1

def cal_tree():
    n,q = map(int,input().split())
    tree = {}
    for i in range(n-1):
        a,b = map(int,input().split())
        if a in tree:
            tree[a].append(b)
        else:
            tree[a] = [b]
    #print(tree)
    #print(tree[1][

=======
Suggestion 2

def solve():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N-1)]
    B = [list(map(int, input().split())) for _ in range(Q)]
    C = [0] * N
    for b in B:
        C[b[0]-1] += b[1]
    for a in A:
        C[a[1]-1] += C[a[0]-1]
    print(*C)

=======
Suggestion 3

def dfs(v, p, d):
    global dst
    dst[v] += d
    for i in range(len(g[v])):
        if g[v][i] == p:
            continue
        dfs(g[v][i], v, d)

n, q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
dst = [0] * n
for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    dfs(p, -1, x)
print(*dst)

=======
Suggestion 4

def dfs(now, pre):
    for i in range(len(tree[now])):
        if tree[now][i] == pre: continue
        dfs(tree[now][i], now)
        cnt[now] += cnt[tree[now][i]]

N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
cnt = [0 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
for _ in range(Q):
    p, x = map(int, input().split())
    cnt[p - 1] += x
dfs(0, -1)
print(' '.join(map(str, cnt)))

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    # 用邻接表表示树
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    # 用数组表示计数器
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
    # 递归计算计数器
    def dfs(tree, counter, node, parent=None):
        for child in tree[node]:
            if child != parent:
                counter[child] += counter[node]
                dfs(tree, counter, child, node)
    dfs(tree, counter, 0)
    print(*counter)

=======
Suggestion 6

def dfs(v, p):
    global cnt
    cnt[v] += cnt[p]
    for i in g[v]:
        if i != p:
            dfs(i, v)

n, q = map(int, input().split())
g = [[] for _ in range(n)]
cnt = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x
dfs(0, 0)
print(*cnt)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def dfs(v):
    global ans
    ans[v] += x
    for i in range(len(child[v])):
        dfs(child[v][i])
    return

N,Q = map(int,input().split())
child = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    child[a-1].append(b-1)

ans = [0] * N
for i in range(Q):
    p,x = map(int,input().split())
    dfs(p-1)

print(*ans)

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    px = [list(map(int, input().split())) for _ in range(q)]
    #print(ab, px)
    #print(n, q)
    #print(px[0][0])
    #print(ab[0][0])
    #print(ab[0][1])
    #print(px[0][1])
    #print(px[1][1])
    #print(px[2][1])
    #print(px[3][1])
    #print(px[4][1])
    #print(px[5][1])
    #print(px[6][1])
    #print(px[7][1])
    #print(px[8][1])
    #print(px[9][1])

    ans = [0] * n
    for i in range(q):
        ans[px[i][0]-1] += px[i][1]

    #print(ans)
    for i in range(n-1):
        if ab[i][0] == 1:
            ans[ab[i][1]-1] += ans[ab[i][0]-1]
        else:
            ans[ab[i][0]-1] += ans[ab[i][1]-1]

    print(*ans)

=======
Suggestion 10

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
