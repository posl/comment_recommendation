Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    M = int(input())
    G = [[0] * 9 for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1][v - 1] = 1
        G[v - 1][u - 1] = 1
    p = list(map(int, input().split()))
    for i in range(8):
        G[p[i] - 1][p[i + 1] - 1] = 1
        G[p[i + 1] - 1][p[i] - 1] = 1
    for i in range(9):
        G[i][i] = 1
    for k in range(9):
        for i in range(9):
            for j in range(9):
                G[i][j] |= G[i][k] & G[k][j]
    if G[0][1] & G[1][2] & G[2][3] & G[3][4] & G[4][5] & G[5][6] & G[6][7] & G[7][8]:
        print(0)
    else:
        print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for _ in range(10)]
    for _ in range(N):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    P = list(map(int, input().split()))
    P.insert(0, 0)

    # 頂点 1 から頂点 i への最短経路を求める
    dist = [float("inf")] * 10
    dist[1] = 0
    que = [1]
    while que:
        u = que.pop(0)
        for v in G[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + 1
                que.append(v)

    # 頂点 1 から頂点 i への最短経路の長さが偶数ならば、
    # コマ i を頂点 1 に移動させることで、最終的に頂点 i に移動させることができる
    ans = 0
    for i in range(1, 9):
        if dist[P[i]] % 2 == 0:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    M = int(input())
    G = [[0]*9 for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1][v-1] = 1
        G[v-1][u-1] = 1
    p = list(map(int, input().split()))
    p = [x-1 for x in p]
    ans = 10**10
    for i in range(9):
        for j in range(i+1, 9):
            for k in range(j+1, 9):
                for l in range(k+1, 9):
                    for m in range(l+1, 9):
                        for n in range(m+1, 9):
                            for o in range(n+1, 9):
                                for r in range(o+1, 9):
                                    for s in range(r+1, 9):
                                        P = [i, j, k, l, m, n, o, r, s]
                                        for t in range(9):
                                            if t not in P:
                                                P.append(t)
                                        flg = True
                                        for t in range(8):
                                            if G[P[t]][P[t+1]] == 0:
                                                flg = False
                                                break
                                        if flg:
                                            cnt = 0
                                            for t in range(8):
                                                if p[t] != P[t]:
                                                    cnt += 1
                                            ans = min(ans, cnt)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    G = [[] for _ in range(10)]
    for _ in range(N):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    P = list(map(int, input().split()))
    for i in range(1, 10):
        G[i].sort()
    ans = 10**10
    for i in range(8):
        for j in range(i+1, 8):
            for k in range(j+1, 8):
                for l in range(k+1, 8):
                    for m in range(l+1, 8):
                        for n in range(m+1, 8):
                            for o in range(n+1, 8):
                                for p in range(o+1, 8):
                                    Q = [P[i], P[j], P[k], P[l], P[m], P[n], P[o], P[p]]
                                    if check(G, Q):
                                        ans = min(ans, bfs(G, Q))
    if ans == 10**10:
        print(-1)
    else:
        print(ans)

=======
Suggestion 5

def main():
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    P = list(map(int,input().split()))
    for i in range(8):
        P[i] -= 1
    INF = 10**10
    dp = [[INF]*9 for _ in range(1<<8)]
    for i in range(8):
        dp[1<<i][P[i]] = 0
    for S in range(1<<8):
        for v in range(9):
            for nv in G[v]:
                for i in range(8):
                    if (S>>i)&1:
                        continue
                    if P[i] == nv:
                        dp[S|(1<<i)][nv] = min(dp[S|(1<<i)][nv],dp[S][v]+1)
    ans = min(dp[(1<<8)-1])
    if ans == INF:
        print(-1)
    else:
        print(ans)

=======
Suggestion 6

def main():
    #入力
    M = int(input())
    G = [[0] * 9 for i in range(9)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u][v] = 1
        G[v][u] = 1
    P = list(map(int, input().split()))
    P = [i - 1 for i in P]
    #print(G)
    #print(P)
    
    #頂点 0 からの最短距離を求める
    dist = [0] * 9
    dist[0] = 1
    queue = [0]
    while queue:
        v = queue.pop(0)
        for i in range(9):
            if G[v][i] and dist[i] == 0:
                dist[i] = dist[v] + 1
                queue.append(i)
    #print(dist)
    
    #頂点 0 からの最短距離が偶数の頂点について、
    #コマが置かれていない頂点にコマを移動させる
    for i in range(9):
        if dist[i] % 2 == 0:
            P[i] = -1
    #print(P)
    
    #コマが置かれていない頂点にコマが置かれている頂点から移動させる
    ans = 0
    for i in range(9):
        if P[i] == -1:
            for j in range(9):
                if P[j] == i:
                    P[j] = -1
                    ans += 1
    #print(P)
    
    #コマが置かれている頂点の番号が頂点の番号と一致しているか判定
    for i in range(9):
        if P[i] != -1 and P[i] != i:
            ans = -1
            break
    print(ans)

main()

=======
Suggestion 7

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    M = int(input())
    graph = [[] for _ in range(10)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, 10):
        graph[i].append(i)
    pos = list(map(int, input().split()))
    for i in range(8):
        pos[i] = [pos[i], i + 1]

    # 連結判定
    def dfs(v):
        seen[v] = True
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)
    seen = [False] * 10
    dfs(1)
    if not all(seen):
        print(-1)
        return

    # 8パズルの距離を求める
    def bfs():
        q = deque()
        q.append(pos)
        d = {(tuple(pos)): 0}
        while q:
            v = q.popleft()
            if v == [[1], [2], [3], [4], [5], [6], [7], [8]]:
                return d[tuple(v)]
            for i in range(8):
                for j in range(8):
                    if i == j:
                        continue
                    if v[i][0] in graph[v[j][0]]:
                        new_v = v[:]
                        new_v[i], new_v[j] = new_v[j], new_v[i]
                        new_v[i].insert(0, new_v[i].pop())
                        new_v[j].insert(0, new_v[j].pop())
                        if tuple(new_v) not in d:
                            d[tuple(new_v)] = d[tuple(v)] + 1
                            q.append(new_v)
        return -1

    print(bfs())

=======
Suggestion 8

def main():
    M = int(input())
    E = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    INF = 10**10
    dp = [[INF] * 9 for _ in range(1 << 8)]
    dp[0][0] = 0
    for s in range(1 << 8):
        for v in range(9):
            for i in range(8):
                if (s >> i) & 1:
                    continue
                for u, w in E:
                    if (P[i] == u and v == w) or (P[i] == w and v == u):
                        dp[s | (1 << i)][P[i] - 1] = min(dp[s | (1 << i)][P[i] - 1], dp[s][v] + 1)
    if dp[-1][-1] == INF:
        print(-1)
    else:
        print(dp[-1][-1])

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n = int(input())
    d = defaultdict(list)
    for i in range(n):
        u,v = map(int,input().split())
        d[u].append(v)
        d[v].append(u)

    s = list(map(int,input().split()))
    for i in range(9):
        if len(d[i+1]) == 0:
            d[i+1] = [-1]
    ans = 0
    for i in range(8):
        if s[i] == i+1:
            continue
        if s[i] in d[s[i+1]]:
            ans += 1
            s[i],s[i+1] = s[i+1],s[i]
        else:
            ans = -1
            break
    print(ans)
