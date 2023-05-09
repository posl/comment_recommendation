def main():
    N, Q = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(N-1)]
    CD = [map(int, input().split()) for _ in range(Q)]
    a, b = [list(i) for i in zip(*AB)]
    c, d = [list(i) for i in zip(*CD)]
    # 隣接リストを作成
    G = [[] for _ in range(N+1)]
    for i in range(N-1):
        G[a[i]].append(b[i])
        G[b[i]].append(a[i])
    # 頂点 1 からの距離を BFS で求める
    dist = [-1]*(N+1)
    dist[1] = 0
    que = [1]
    while que:
        v = que.pop()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v]+1
            que.append(nv)
    # 各クエリについて答える
    for i in range(Q):
        if (dist[c[i]]+dist[d[i]]) % 2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()