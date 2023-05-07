def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 9)
    
    MOD = 10**9+7
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    # 1 から N への最短距離
    dist = [0] * (N+1)
    dist[1] = 1
    # 1 から N への経路数
    path = [0] * (N+1)
    path[1] = 1
    # 1 から N への経路
    route = [[] for _ in range(N+1)]
    route[1] = [1]
    # 1 から N への経路を探索
    que = deque([1])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] == 0:
                dist[nv] = dist[v] + 1
                path[nv] = path[v]
                route[nv] = route[v] + [nv]
                que.append(nv)
            elif dist[nv] == dist[v] + 1:
                path[nv] += path[v]
                path[nv] %= MOD
    print(path[N])

if __name__ == '__main__':
    main()