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

if __name__ == '__main__':
    main()