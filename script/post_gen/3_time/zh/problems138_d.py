Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(node, parent):
    for i in node:
        if i != parent:
            dfs(i, node)
            for j in range(len(node)):
                if node[j] == i:
                    node[j] = node[j] + node[i]

=======
Suggestion 2

def dfs(v, p, x):
    global ans
    ans[v] += x
    for u in g[v]:
        if u != p:
            dfs(u, v, x)

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

ans = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    dfs(p - 1, -1, x)

print(*ans)

=======
Suggestion 3

def dfs(v):
    visited[v] = True
    for j in range(len(G[v])):
        if visited[G[v][j][0]] == False:
            ans[G[v][j][0]] += ans[v] + G[v][j][1]
            dfs(G[v][j][0])
    return

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
visited = [False for _ in range(N)]
ans = [0 for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append((b - 1, 1))
    G[b - 1].append((a - 1, 1))

for _ in range(Q):
    p, x = map(int, input().split())
    ans[p - 1] += x

dfs(0)

for i in range(N):
    print(ans[i], end = ' ')

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    ans = [0] * N
    for _ in range(N - 1):
        a, b = map(int, input().split())
        ans[a - 1] += 1
        ans[b - 1] += 1
    for _ in range(Q):
        p, x = map(int, input().split())
        ans[p - 1] += x
    print(*ans)

=======
Suggestion 5

def dfs(v, p):
    for i in to[v]:
        if i != p:
            cnt[i] += cnt[v]
            dfs(i, v)

n, q = map(int, input().split())
to = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
cnt = [0] * n
for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x
dfs(0, -1)
print(*cnt)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def dfs(n, x, p, t, c, d):
    for i in t[n]:
        if i != p:
            c[i] += x[n]
            dfs(i, x, n, t, c, d)
    return c

=======
Suggestion 8

def dfs(node, parent):
    global ans
    ans[node] += ans[parent]
    for child in tree[node]:
        if child != parent:
            dfs(child, node)

N, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
ans = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    ans[p] += x

dfs(1, 0)
print(*ans[1:])

=======
Suggestion 9

def main():
    n,q = map(int, input().split())
    ab = [[0]*2 for i in range(n-1)]
    for i in range(n-1):
        ab[i][0],ab[i][1] = map(int, input().split())
    px = [[0]*2 for i in range(q)]
    for i in range(q):
        px[i][0],px[i][1] = map(int, input().split())
    #print(px)
    #print(ab)
    #print(n,q)
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    #print(ab[2][0])
    #print(ab[2][1])
    #print(px[0][0])
    #print(px[0][1])
    #print(px[1][0])
    #print(px[1][1])
    #print(px[2][0])
    #print(px[2][1])
    #print(px[3][0])
    #print(px[3][1])
    #print(px[4][0])
    #print(px[4][1])
    #print(px[5][0])
    #print(px[5][1])
    #print(px[6][0])
    #print(px[6][1])
    #print(px[7][0])
    #print(px[7][1])
    #print(px[8][0])
    #print(px[8][1])
    #print(px[9][0])
    #print(px[9][1])
    #print(px[10][0])
    #print(px[10][1])
    #print(px[11][0])
    #print(px[11][1])
    #print(px[12][0])
    #print(px[12][1])
    #print(px[13][0])
    #print(px[13][1])
    #print(px[14][0])
    #print(px[14][1])
    #print(px[15][0])
    #print(px[15][1])
    #print(px[16][0])
    #print(px[16][1])
    #print(px[17][0])
    #print(px[17][1])
    #print(px[18][0])
    #

=======
Suggestion 10

def main():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    points = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        points[p-1] += x
    queue = [0]
    while queue:
        p = queue.pop()
        for i in tree[p]:
            if points[i] == 0:
                points[i] = points[p]
                queue.append(i)
    print(*points)
