Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in A or N not in B:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in B or N not in A:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in A and N not in B:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in B and N not in A:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in A and N not in A:
        print(0)
        return
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if 1 not in B and N not in B:
        print(0)
        return

    # 都市 1 から都市 N へ移動することが出来る場合は 1 と出力せよ。
    if 1 in A and N in B:
        print(1)
        return
    # 都市 1 から都市 N へ移動することが出来る場合は 1 と出力せよ。
    if 1 in B and

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    road = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        road[A-1].append(B-1)
        road[B-1].append(A-1)
    print(road)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    INF = 10**9
    dist = [INF for _ in range(N+1)]
    dist[1] = 0
    que = [1]
    while que:
        v = que.pop(0)
        for nv in G[v]:
            if dist[nv] > dist[v] + 1:
                dist[nv] = dist[v] + 1
                que.append(nv)
    if dist[N] == INF:
        print(0)
        return
    cnt = 0
    que = [N]
    while que:
        v = que.pop(0)
        for nv in G[v]:
            if dist[nv] == dist[v] - 1:
                cnt += 1
                que.append(nv)
    print(cnt)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    # 隣接リスト
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    # 都市 1 から都市 N への移動に必要な時間
    time = [-1] * N
    # 都市 1 から都市 N への移動に必要な時間の最小値
    min_time = -1
    # 都市 1 から都市 N への移動に必要な時間の最小値を実現する経路の数
    min_time_path = 0
    # 幅優先探索
    que = [0]
    time[0] = 0
    while que:
        # キューの先頭を取り出す
        v = que.pop(0)
        # キューの先頭から移動可能な都市を順に探索
        for nv in graph[v]:
            # まだ探索していない都市の場合
            if time[nv] == -1:
                # キューの末尾に追加
                que.append(nv)
                # その都市に移動するのに必要な時間を更新
                time[nv] = time[v] + 1
                # 最小値を更新した場合
                if min_time == -1 or time[nv] < min_time:
                    min_time = time[nv]
                    min_time_path = 1
                # 最小値と同じ場合
                elif time[nv] == min_time:
                    min_time_path += 1
    print(min_time_path)

=======
Suggestion 5

def main():
    import sys
    from collections import deque
    #入力
    readline = sys.stdin.buffer.readline
    def map_readline(): return map(int, readline().split())
    N, M = map_readline()
    if M == 0:
        print(0)
        sys.exit()
    road = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map_readline()
        road[a-1].append(b-1)
        road[b-1].append(a-1)

    #都市1から都市Nへの最短経路を求める
    INF = 10**9
    dist = [INF] * N
    dist[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in road[v]:
            if dist[nv] != INF:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)

    #都市1から都市Nへの最短経路の数を求める
    ans = 0
    que = deque([N-1])
    while que:
        v = que.popleft()
        if v == 0:
            ans += 1
        for nv in road[v]:
            if dist[nv] != dist[v] - 1:
                continue
            que.append(nv)
    print(ans % (10**9+7))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    # 都市間の距離
    dist = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        dist[a-1][b-1] = dist[b-1][a-1] = 1
    # ワーシャルフロイド法
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # 経路の数
    route = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dist[i][j] == 2:
                route[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if route[i][k] > 0 and route[k][j] > 0:
                    route[i][j] += route[i][k] * route[k][j]
    print(route[0][N-1] % (10**9+7))

=======
Suggestion 7

def main():
    import sys
    readline = sys.stdin.readline
    from collections import deque
    from itertools import permutations
    mod = 10**9+7

    N,M = map(int,readline().split())
    # 隣接リスト
    G = [[] for _ in range(N)]
    for i in range(M):
        a,b = map(int,readline().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # 1からNまでの最短距離を求める
    dist = [-1]*N
    dist[0] = 0
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)

    # 1からNまでの最短距離がKのものを数える
    K = dist[N-1]
    cnt = 0
    for i in range(N):
        if dist[i] == K:
            cnt += 1

    # 1からNまでの最短距離がKのもののうち、1からNまでの最短経路を数える
    ans = 1
    for i in range(N):
        if dist[i] == K:
            ans = ans*len(G[i])
            ans %= mod

    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # 都市間の道路情報を格納するリスト
    roadlist = [[] for i in range(N)]
    # 道路数が0の場合は0を出力
    if M == 0:
        print(0)
        return

    # 道路情報をリストに格納
    for i in range(M):
        a, b = map(int, input().split())
        roadlist[a - 1].append(b - 1)
        roadlist[b - 1].append(a - 1)

    # 都市1から都市Nへの最短経路を格納するリスト
    shortest = [0] * N
    # 都市1から都市Nへの最短経路の数を格納するリスト
    shortestcount = [0] * N
    # 都市1から都市Nへの最短経路の数を格納するリストの初期値を1にする
    shortestcount[0] = 1

    # 都市1から都市Nへの最短経路を探索する
    for i in range(N):
        # 都市1から都市Nへの最短経路が探索済みの場合は処理をスキップ
        if shortest[i] != 0:
            continue
        # 都市1から都市Nへの最短経路を探索する
        for j in range(N):
            # 都市1から都市Nへの最短経路を探索済みの場合は処理をスキップ
            if shortest[j] != 0:
                continue
            # 都市1から都市Nへの最短経路が探索済みの場合は処理をスキップ
            if shortestcount[j] != 0:
                continue
            # 都市1から都市N

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 都市の数
    # 道路の数
    # 都市の数は 2 以上 2× 10^5 以下
    # 道路の数は 0 以上 2× 10^5 以下
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if N == 2:
        # 都市 1 から都市 2  に移動することはできません。この場合 0 を出力してください。
        print(0)
        return

    # 都市 1 から都市 N へ最も早く移動することができる経路は何通りありますか？
    # 経路は 1 -> 3 -> 2 -> 4 の 1 つです。
    # 1 から 3 に移動する時間は 1 時間
    # 3 から 2 に移動する時間は 1 時間
    # 2 から 4 に移動する時間は 1 時間
    # 1 から 4 に移動する時間は 3 時間
    # 都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    # 経路は 1 -> 3 -> 2 -> 4 の 1 つです。
    # 1 から 3 に移動する時間は 1 時間
    # 3 から 2 に移動する時間は 1 時間
    # 2 から 4 に移動する時間は 1 時間
    # 1 から 4 に移動する時間は 3 時間
    # 道路 i を通ると都市 A_i と都市 B_i の間を双方向に 1 時間で移動する

=======
Suggestion 10

def solve(N, M, AB):
    import sys
    sys.setrecursionlimit(10**6)
    mod = 10**9+7
    # 入力
    # 隣接リスト
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 探索
    # 1からNへの最短経路の個数
    # BFS
    from collections import deque
    # キュー
    queue = deque()
    queue.append(0)
    # 訪問済み
    visited = [False]*N
    visited[0] = True
    # 遷移元
    prev = [-1]*N
    # 遷移元からの距離
    dist = [-1]*N
    dist[0] = 0
    # BFS
    while queue:
        # キューから取り出す
        now = queue.popleft()
        # 隣接リストを調べる
        for next in G[now]:
            if visited[next]:
                continue
            # 訪問済みにする
            visited[next] = True
            # キューに入れる
            queue.append(next)
            # 遷移元を記録
            prev[next] = now
            # 遷移元からの距離を記録
            dist[next] = dist[now]+1
    # 出力
    if dist[N-1] == -1:
        print(0)
    else:
        # 1からNへの最短経路
        path = []
        now = N-1
        while now != -1:
            path.append(now)
            now = prev[now]
        path.reverse()
        # 1からNへの最短経路の個数
        # 各都市の遷移元の数
        num = [0]*N
        num[0] = 1
        for i in range(1, N):
            num[i] = 1
