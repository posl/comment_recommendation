def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    # 隣接リスト
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
    # 頂点 0 から各頂点への距離
    dist = [0] * N
    # 幅優先探索
    from collections import deque
    q = deque([0])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == 0:
                dist[nv] = dist[v] + 1
                q.append(nv)
    # 頂点 0 から各頂点への距離が 2 以上のものの個数を数える
    print(sum(1 for d in dist if d >= 2))

if __name__ == '__main__':
    main()