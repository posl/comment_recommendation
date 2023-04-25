Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)
    MOD = 10**9 + 7
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    if dist[N-1] == -1:
        print(0)
        return
    cnt = [0] * N
    cnt[N-1] = 1
    q = [N-1]
    while q:
        v = q.pop()
        for nv in G[v]:
            if dist[nv] != dist[v] - 1:
                continue
            cnt[nv] += cnt[v]
            cnt[nv] %= MOD
            q.append(nv)
    print(cnt[0])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    MOD = 10**9 + 7
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        for j in edges[i]:
            dp[j] += dp[i]
            dp[j] %= MOD
    print(dp[-1])

=======
Suggestion 3

def main():
    #input
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    #solve
    ans = 0

    #output
    print(ans)

=======
Suggestion 4

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    MOD = 10 ** 9 + 7
    dist = [-1] * N
    dist[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for to in G[v]:
            if dist[to] != -1:
                continue
            dist[to] = dist[v] + 1
            q.append(to)

    if dist[-1] == -1:
        print(0)
        return

    cnt = [0] * N
    cnt[-1] = 1
    q = deque([N - 1])
    while q:
        v = q.popleft()
        for to in G[v]:
            if dist[to] != dist[v] - 1:
                continue
            cnt[to] += cnt[v]
            cnt[to] %= MOD
            q.append(to)

    print(cnt[0])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if N == 2:
        if M == 0:
            print(0)
        else:
            print(1)
        return
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        G[B].append(A)
    MOD = 10**9 + 7
    D = [0] * (N + 1)
    D[1] = 1
    Q = [1]
    while Q:
        n = Q.pop()
        for m in G[n]:
            if D[m] == 0:
                D[m] = D[n] + 1
                Q.append(m)
    if D[N] == 0:
        print(0)
        return
    P = [0] * (N + 1)
    P[N] = 1
    Q = [N]
    while Q:
        n = Q.pop()
        for m in G[n]:
            if D[m] == D[n] - 1:
                P[m] = (P[m] + P[n]) % MOD
                Q.append(m)
    print(P[1])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if N == 2:
        print(0)
        return
    if M == 0:
        print(0)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    adj = [[] for _ in range(N)]
    for i in range(M):
        adj[AB[i][0]-1].append(AB[i][1]-1)
        adj[AB[i][1]-1].append(AB[i][0]-1)
    #print(adj)
    visited = [0] * N
    visited[0] = 1
    count = [0] * N
    count[0] = 1
    stack = [0]
    while len(stack) > 0:
        u = stack.pop()
        for v in adj[u]:
            if visited[v] == 0:
                visited[v] = 1
                count[v] = count[u]
                stack.append(v)
            elif visited[v] == 1:
                count[v] += count[u]
    print(count[N-1]%(10**9+7))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())

    # 隣接リストを作る
    adj = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        adj[A].append(B)
        adj[B].append(A)

    # 各頂点について、1からの距離を計算する
    # 1からの距離が1の頂点は、1からの最短経路の数は1
    # 1からの距離が2の頂点は、1からの最短経路の数は1からの距離が1の頂点の数
    # 1からの距離が3の頂点は、1からの最短経路の数は1からの距離が1の頂点の数 + 1からの距離が2の頂点の数
    # というように、1からの距離がiの頂点は、1からの距離がi-1の頂点の数となる
    # このように、1からの距離がiの頂点は、1からの距離がi-1の頂点の数となることを利用する
    # 1からの距離がiの頂点の数を、dp[i]とすると、dp[i] = dp[i-1] + dp[i-2]となる
    # dp[0] = 1, dp[1] = 0とする
    # dp[N-1]が、1からNまでの最短経路の数となる
    dp = [0] * (N + 1)
    dp[0] = 1

    # 1から幅優先探索を行う
    # 1からの距離がiの頂点の数を、dp[i

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 1から各頂点への最短距離を求める
    # 隣接行列を作成
    adj = [[0] * N for _ in range(N)]
    for a, b in AB:
        adj[a - 1][b - 1] = 1
        adj[b - 1][a - 1] = 1

    # ダイクストラ法
    d = [float("inf")] * N
    d[0] = 0
    q = [0]
    while q:
        u = q.pop(0)
        for v in range(N):
            if adj[u][v] == 1 and d[v] > d[u] + 1:
                d[v] = d[u] + 1
                q.append(v)

    # 最短距離がN-1の頂点数を求める
    print(d.count(N - 1))
