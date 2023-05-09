def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    MOD = 10 ** 9 + 7
    dist = [-1] * N
    dist[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for to in G[v]:
            if dist[to] != -1:
                continue
            dist[to] = dist[v] + 1
            q.append(to)
    if dist[-1] == -1:
        print(0)
        return
    cnt = [0] * N
    cnt[-1] = 1
    q = deque([N - 1])
    while q:
        v = q.popleft()
        for to in G[v]:
            if dist[to] != dist[v] - 1:
                continue
            cnt[to] += cnt[v]
            cnt[to] %= MOD
            q.append(to)
    print(cnt[0])

if __name__ == '__main__':
    main()