Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

seen = [False]*n
ans = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    u = [0]*m
    v = [0]*m
    for i in range(m):
        u[i],v[i] = map(int,input().split())
    print(n-1)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    visited = [False for _ in range(n)]
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        cnt += 1
        visited[i] = True
        q = [i]
        while q:
            v = q.pop()
            for u in g[v]:
                if visited[u]:
                    continue
                visited[u] = True
                q.append(u)
    print(cnt)

=======
Suggestion 4

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    visited = [False]*N

    def dfs(v):
        visited[v] = True
        for nv in G[v]:
            if not visited[nv]:
                dfs(nv)

    ans = 0
    for v in range(N):
        if not visited[v]:
            dfs(v)
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    v = [0]*n
    def dfs(x):
        v[x] = 1
        for i in g[x]:
            if v[i] == 0:
                dfs(i)
    ans = 0
    for i in range(n):
        if v[i] == 0:
            dfs(i)
            ans += 1
    print(ans)

=======
Suggestion 7

def dfs(x):
    seen[x] = True
    for i in edge[x]:
        if not seen[i]:
            dfs(i)

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

seen = [False] * n
ans = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        ans += 1

print(ans)

=======
Suggestion 8

def main():
    #n = int(input())
    #a, b = map(int, input().split())
    n, m = map(int, input().split())
    #s = input()
    #s = input().split()
    #a = list(map(int, input().split()))
    #a = [int(input()) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [input() for i in range(n)]
    #a = [input().split() for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [[int(input()) for i in range(n)] for j in range(n)]
    #a = [[int(input()) for i in range(m)] for j in range(n)]
    #a = [[input() for i in range(n)] for j in range(n)]
    #a = [[input().split() for i in range(n)] for j in range(n)]
    #a = [[list(map(int, input().split())) for i in range(m)] for j in range(n)]
    #a = [list(map(int, input().split())) for i in range(m)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [input() for i in range(n)]
    #a = [input().split() for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [int(input()) for i in range(n)]
    #a = [input() for i in range(n)]
    #a = [input().split() for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [[int(input()) for i in range(n)] for j in range(n)]
    #a = [[input() for i in range(n)] for j in range(n)]
    #a = [[input().split() for i in range

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    #print(n, m)
    #print(a)

    # グラフの作成
    graph = [[] for i in range(n)]
    for i in range(m):
        graph[a[i][0]-1].append(a[i][1]-1)
        graph[a[i][1]-1].append(a[i][0]-1)
    #print(graph)

    # 深さ優先探索
    def dfs(v):
        seen[v] = True
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)

    # 連結成分の数を数える
    seen = [False] * n
    count = 0
    for v in range(n):
        if seen[v]:
            continue
        dfs(v)
        count += 1
    print(count)

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    #print(N,
