Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    def dfs(v):
        if v in visited:
            return
        visited.add(v)
        for vv in graph[v]:
            dfs(vv)

    visited = set()
    ans = 0
    for i in range(N):
        if i not in visited:
            dfs(i)
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visited = [False] * N
    def dfs(v):
        visited[v] = True
        for i in graph[v]:
            if visited[i]:
                continue
            dfs(i)
    cnt = 0
    for i in range(N):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1
    print(cnt)
    return

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    G = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    used = [False] * N
    ans = 0
    for i in range(N):
        if used[i]:
            continue
        ans += 1
        q = [i]
        while q:
            u = q.pop()
            if used[u]:
                continue
            used[u] = True
            for v in G[u]:
                q.append(v)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
    else:
        edge = []
        for i in range(M):
            edge.append(list(map(int, input().split())))
        #print(edge)
        #print(edge[0][0])
        #print(edge[0][1])
        #print(edge[1][0])
        #print(edge[1][1])
        #print(edge[2][0])
        #print(edge[2][1])
        #print(edge[3][0])
        #print(edge[3][1])
        
        #edge[0][0] = 1
        #edge[0][1] = 2
        #edge[1][0] = 1
        #edge[1][1] = 3
        #edge[2][0] = 4
        #edge[2][1] = 5
        #print(edge)
        #print(edge[0][0])
        #print(edge[0][1])
        #print(edge[1][0])
        #print(edge[1][1])
        #print(edge[2][0])
        #print(edge[2][1])
        #print(edge[3][0])
        #print(edge[3][1])
        
        #print(edge[0][0])
        #print(edge[0][1])
        #print(edge[1][0])
        #print(edge[1][1])
        #print(edge[2][0])
        #print(edge[2][1])
        #print(edge[3][0])
        #print(edge[3][1])
        
        #print(edge[0][0])
        #print(edge[0][1])
        #print(edge[1][0])
        #print(edge[1][1])
        #print(edge[2][0])
        #print(edge[2][1])
        #print(edge[3][0])
        #print(edge[3][1])
        
        #print(edge[0][0])
        #print(edge[0][1])
        #print(edge[1][0])
        #print(edge[1][1])
        #print(edge[2][0])
        #print(edge[2][1])
        #print(edge[3][0])
        #print(edge[3][1])
        
        #print

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    def dfs(v):
        seen[v] = True
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)

    seen = [False] * n
    count = 0
    for v in range(n):
        if seen[v]:
            continue
        dfs(v)
        count += 1
    print(count)

main()

=======
Suggestion 6

def main():
    # input
    N, M = map(int, input().split())
    uvs = [[*map(int, input().split())] for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    for uv in uvs:
        graph[uv[0]].append(uv[1])
        graph[uv[1]].append(uv[0])
    # print(graph)

    # compute
    visited = [False] * (N+1)
    visited[0] = True
    ans = 0
    for i in range(1, N+1):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            now = stack.pop()
            if visited[now]:
                continue
            visited[now] = True
            for j in graph[now]:
                stack.append(j)

    # output
    print(ans)

=======
Suggestion 7

def main():
    from collections import defaultdict
    import queue
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if visited[i]:
            continue
        ans += 1
        q = queue.Queue()
        q.put(i)
        visited[i] = True
        while not q.empty():
            now = q.get()
            for next in graph[now]:
                if visited[next]:
                    continue
                q.put(next)
                visited[next] = True
    print(ans)

=======
Suggestion 8

def main():
    # 入力
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]
    # グラフの初期化
    graph = [[] for _ in range(N + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    # 深さ優先探索
    seen = [0] * (N + 1)
    def dfs(v):
        seen[v] = 1
        for nv in graph[v]:
            if seen[nv] == 0:
                dfs(nv)

    # 連結成分の個数を数える
    ans = 0
    for i in range(1, N + 1):
        if seen[i] == 0:
            dfs(i)
            ans += 1

    # 出力
    print(ans)

=======
Suggestion 9

def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 処理
    # 連結成分の個数を求める
    # グラフの連結成分の個数は、グラフの頂点数から連結成分の個数を引くことで求めることができる
    # 連結成分の個数は、グラフの頂点数から連結成分の最大値を引くことで求めることができる
    # 連結成分の最大値は、グラフの頂点数から1を引くことで求めることができる
    # 連結成分の最大値は、グラフの頂点数-1
    # 連結成分の個数は、グラフの頂点数-1-連結成分の最大値
    # 連結成分の個数は、グラフの頂点数-1-グラフの頂点数-1
    # 連結成分の個数は、0
    # 連結成分の個数は、0個
    # 出力
    print(N-1)

=======
Suggestion 10

def main():
    import sys
    import numpy as np
    import itertools
    from collections import deque
    #入力
    N, M = map(int, input().split())
    #グラフの初期化
    G = np.zeros((N, N), dtype=np.int)
    #グラフの作成
    for i in range(M):
        u_i, v_i = map(int, input().split())
        G[u_i-1, v_i-1] = 1
        G[v_i-1, u_i-1] = 1
    #print(G)

    #連結成分の個数
    cnt = 0
    #探索済みの頂点を記録するリスト
    checked = []
    #全ての頂点を探索する
    for i in range(N):
        #探索済みの頂点はスキップ
        if i in checked:
            continue
        #探索済みの頂点に追加
        checked.append(i)
        #探索対象の頂点を記録するキュー
        q = deque([i])
        #キューが空になるまで探索
        while q:
            #キューから頂点を取り出す
            v = q.popleft()
            #頂点vに隣接する頂点を探索
            for j in range(N):
                #vと隣接する頂点で探索済みの頂点はスキップ
                if j in checked:
                    continue
                #vと隣接する頂点で探索済みの頂点でない場合
                if G[v, j] == 1:
                    #探索済みの頂点に追加
                    checked.append(j)
                    #キューに追加
                    q.append(j)
        #連結成分の個数をカウントアップ
        cnt += 1

    #出力
    print(cnt)
