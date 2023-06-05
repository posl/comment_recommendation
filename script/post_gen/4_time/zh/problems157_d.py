Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dfs(u, p):
    global ans
    for v in g[u]:
        if v == p:
            continue
        if v in s:
            ans[v] -= 1
        else:
            ans[v] += 1
        dfs(v, u)

n, m, k = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

s = set()
for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if c > d:
        c, d = d, c
    if c == 0 and d == n - 1:
        s.add(d)
    else:
        g[c].append(d)
        g[d].append(c)

ans = [0] * n
dfs(0, -1)
print(*ans)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for _ in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    # print(N, M, K)
    # print(A)
    # print(B)
    # print(C)
    # print(D)

    # 建立图
    graph = {}
    for i in range(M):
        if A[i] not in graph:
            graph[A[i]] = [B[i]]
        else:
            graph[A[i]].append(B[i])
        if B[i] not in graph:
            graph[B[i]] = [A[i]]
        else:
            graph[B[i]].append(A[i])
    # print(graph)

    # 计算每个节点的候选好友
    ans = [0] * N
    for i in range(1, N + 1):
        if i in graph:
            for j in graph[i]:
                if j not in graph:
                    continue
                for k in graph[j]:
                    if k not in graph:
                        continue
                    if k != i and k not in graph[i]:
                        ans[i - 1] += 1
    print(' '.join(map(str, ans)))

=======
Suggestion 4

def main():
    n,m,k = map(int, input().split())

    # 建立邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    # 建立阻隔表
    block = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        c,d = map(int, input().split())
        block[c-1][d-1] = True
        block[d-1][c-1] = True

    # 深度优先搜索
    ans = [0 for _ in range(n)]
    for i in range(n):
        visited = [False for _ in range(n)]
        visited[i] = True
        stack = [i]
        while stack:
            s = stack.pop()
            for j in adj[s]:
                if visited[j]: continue
                if block[s][j]: continue
                ans[i] += 1
                visited[j] = True
                stack.append(j)

    print(*ans)
    return

=======
Suggestion 5

def dfs(v, c):
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == c:
            return False
        if color[graph[v][i]] == 0 and (not dfs(graph[v][i], -c)):
            return False
    return True

n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
color = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for i in range(n):
    if color[i] == 0:
        if not dfs(i, 1):
            print(-1)
            exit()

cnt = [0] * n
for i in range(n):
    cnt[i] = len(graph[i])

for i in range(k):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        cnt[c - 1] -= 1
        cnt[d - 1] -= 1

print(*cnt)

=======
Suggestion 6

def main():
    n,m,k = map(int,input().split())
    a = [0] * (n+1)
    b = [0] * (n+1)
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(k):
        c[i],d[i] = map(int,input().split())
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(k):
        c[i],d[i] = map(int,input().split())
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(k):
        c[i],d[i] = map(int,input().split())
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(k):
        c[i],d[i] = map(int,input().split())
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(k):
        c[i],d[i] = map(int,input().split())
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(k):
        c[i],d[i] = map(int,input().split())
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(k):
        c[i],d[i] = map(int,input().split())

=======
Suggestion 7

def dfs(g, v, u, d, c):
    if d == 0:
        c[v] = 1
        return
    for w in g[v]:
        if w == u:
            continue
        dfs(g, w, v, d - 1, c)
