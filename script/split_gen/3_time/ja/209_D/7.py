def main():
    # 入力
    N,Q = map(int,input().split())
    # 隣接リスト
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 根からの距離
    dist = [-1]*N
    dist[0] = 0
    # BFS
    que = [0]
    while que:
        v = que.pop()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)
    # 出力
    for _ in range(Q):
        c,d = map(int,input().split())
        if abs(dist[c-1]-dist[d-1])%2 == 0:
            print("Town")
        else:
            print("Road")
