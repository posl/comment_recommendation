def main():
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N - 1)]
    cd = [list(map(int, input().split())) for _ in range(Q)]
    graph = [[] for _ in range(N)]
    for a, b in ab:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # 1. 全ての頂点からの最短距離を求める
    from collections import deque
    dist = [-1] * N
    dist[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in graph[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    # 2. 各クエリについて、距離の偶奇が一致しているかで判定する
    for c, d in cd:
        if dist[c - 1] % 2 == dist[d - 1] % 2:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()