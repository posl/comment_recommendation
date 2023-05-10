def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(N, M)
    # print(A)
    # print(B)
    # print('-------------')
    # 頂点番号を1から始めるために、各要素を-1する
    A = list(map(lambda x: x-1, A))
    B = list(map(lambda x: x-1, B))
    # print(A)
    # print(B)
    # print('-------------')
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for i in range(M):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
    # print(adj)
    # print('-------------')
    # 頂点1からの距離
    dist = [-1] * N
    # 頂点1からの距離を0にする
    dist[0] = 0
    # 幅優先探索
    queue = [0]
    while len(queue) > 0:
        # 先頭の頂点を取り出す
        v = queue.pop(0)
        # vから行ける頂点を探索
        for u in adj[v]:
            # 未訪問の場合
            if dist[u] == -1:
                # 頂点uへの距離を更新
                dist[u] = dist[v] + 1
                # キューに追加
                queue.append(u)
    # print(dist)
    # print('-------------')
    # 頂点1からの距離が偶数の頂点の数
    n1 = 0
    # 頂点1からの距離が奇数の頂点の数
    n2 = 0
    for i in range(N):
        if dist[i] % 2 == 0:
            n1 += 1
        else:
            n2 += 1
    # print
