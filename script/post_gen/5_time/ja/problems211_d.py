Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    mod = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for a, b in AB:
            if b == i:
                dp[i] += dp[a]
                dp[i] %= mod
    print(dp[N])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]

    # 隣接リスト
    adj = [[] for _ in range(n)]
    for a, b in ab:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    # 頂点 0 から各頂点への最短距離
    dist = [-1] * n
    dist[0] = 0

    # 頂点 0 から各頂点への最短経路数
    cnt = [0] * n
    cnt[0] = 1

    # 幅優先探索
    from collections import deque
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            cnt[nv] = cnt[v]
            q.append(nv)
        # 頂点 0 から頂点 n-1 への最短経路が求まったら探索を終了
        if dist[n-1] != -1:
            break

    print(cnt[n-1] % (10**9+7))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())

    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)

    # 頂点1からの最短経路長
    dist = [0] * N

    # 頂点1からの最短経路数
    count = [0] * N
    count[0] = 1

    # 幅優先探索
    from collections import deque
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in adj[v]:
            if dist[nv] == 0:
                dist[nv] = dist[v] + 1
                que.append(nv)
            if dist[nv] == dist[v] + 1:
                count[nv] += count[v]
                count[nv] %= 10 ** 9 + 7

    print(count[N - 1])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(A)
    print(B)
    return

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    if n == 2:
        print(0)
        exit()
    if m == 0:
        print(0)
        exit()

    # 都市間の道路をリストで表現
    road = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)

    # 1から各都市への最短経路数をリストで表現
    # 1からの距離を表す
    dist = [0 for _ in range(n)]
    dist[0] = 1
    # 1から各都市への最短経路数を表す
    # 1からの距離が同じ都市の数を表す
    dist_cnt = [0 for _ in range(n)]
    dist_cnt[0] = 1
    # 1からの距離が1の都市をキューに入れる
    queue = [0]

    # 幅優先探索
    while len(queue) > 0:
        # 1からの距離が1の都市を取り出す
        x = queue.pop(0)
        # 1からの距離が1の都市に隣接する都市を調べる
        for y in road[x]:
            # 1からの距離が未確定の場合
            if dist[y] == 0:
                # 1からの距離を更新
                dist[y] = dist[x] + 1
                # 1からの距離が1の都市の数を更新
                dist_cnt[y] = dist_cnt[x]
                # 1からの距離が1の都市をキューに入れる
                queue.append(y)
            # 1からの距離が確定している場合
            elif dist[y] == dist[x] +

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N, M, A, B)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(A)
    print(B)
    #for i in range(M):
    #    print(A[i], B[i])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    #print(N, M, AB)

    # 都市1から都市Nへの経路を求める
    # 都市1からの経路を順に探索していく
    # 経路を見つけると、その道を通った経路が見つかったとして、
    # その道を通ることで経路が見つかった都市の経路数を足す
    # すでにその道を通った経路が見つかっている場合は、その経路数を足す
    # すべての経路が見つかったら終了
    # 経路数は、道の経路数の和の経路数
    # 道の経路数は、道を通った経路数の和の経路数
    # 道を通った経路数は、都市の経路数の和の経路数
    # 都市の経路数は、都市の経路数の和の経路数
    # すべての経路が見つかったら終了
    # すべての経路が見つかるまで、すべての道を探索する
    # すべての道を探索したら、すべての経路が見つかったことになる

    # まず道を探索する
    # 道を探索すると、その道を通った経路が見つかったとして、
    # その道を通ることで経路が見つかった都市の経路数を足す
    # すでにその道を通った経路が見つかって

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    print(AB)
