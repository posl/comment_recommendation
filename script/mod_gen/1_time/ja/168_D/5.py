def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    # 1からの距離
    dist = [-1]*(N+1)
    dist[1] = 0
    # BFS
    q = deque([1])
    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = v
            q.append(nv)
    # 出力
    if -1 in dist[2:]:
        print("No")
    else:
        print("Yes")
        for i in range(2, N+1):
            print(dist[i])

if __name__ == '__main__':
    main()