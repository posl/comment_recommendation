Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]

    out = [0] * n
    out[0] = 1
    for a, b in ab:
        if out[a - 1] == 1:
            out[b - 1] = a
        elif out[b - 1] == 1:
            out[a - 1] = b

    if 0 in out:
        print('No')
    else:
        print('Yes')
        for i in range(1, n):
            print(out[i])

=======
Suggestion 3

def dfs(node, parent):
    global G, ans
    for i in G[node]:
        if i == parent:
            continue
        if ans[i] != 0:
            continue
        ans[i] = node
        dfs(i, node)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

ans = [0] * (N+1)
ans[1] = 1
dfs(1, -1)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        a, b = map(int, input().split())
        ab.append((a, b))

    # print(ab)

    # 1からの最短経路を求める
    from collections import deque
    adj = [[] for _ in range(n + 1)]
    for a, b in ab:
        adj[a].append(b)
        adj[b].append(a)

    # print(adj)

    dist = [-1] * (n + 1)
    dist[1] = 0
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            queue.append(nv)

    # print(dist)

    # 1からの最短経路から逆算していく
    ans = [0] * (n + 1)
    for a, b in ab:
        # 1からの最短経路が繋がっているか
        if dist[a] == dist[b] + 1:
            ans[a] = b
        if dist[b] == dist[a] + 1:
            ans[b] = a

    # print(ans)

    # 全部埋まっているか
    if 0 in ans[2:]:
        print("No")
    else:
        print("Yes")
        for i in range(2, n + 1):
            print(ans[i])

=======
Suggestion 5

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if visited[next_v]:
            continue
        dfs(next_v)
        if dp[next_v] == 0:
            dp[v] = next_v
            return
        elif dp[v] == 0:
            dp[v] = dp[next_v]
        else:
            dp[v] = -1

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dp = [0] * (n + 1)
dfs(1)

=======
Suggestion 6

def dfs(u, p):
    for v in to[u]:
        if v == p:
            continue
        if mark[v] == 0:
            mark[v] = u
            dfs(v, u)
        else:
            if ans[v] == 0:
                t = u
                while t != v:
                    ans[t] = mark[t]
                    t = mark[t]
                ans[v] = mark[v]
                print("Yes")
                for i in range(1, n + 1):
                    print(ans[i])
                exit()
            else:
                continue
    return

n, m = map(int, input().split())
to = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    to[a].append(b)
    to[b].append(a)
mark = [0] * (n + 1)
ans = [0] * (n + 1)
mark[1] = -1
dfs(1, -1)
print("No")

=======
Suggestion 7

def solve():
    pass
