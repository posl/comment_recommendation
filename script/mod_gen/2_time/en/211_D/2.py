def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    MOD = 10 ** 9 + 7
    dist = [-1] * N
    dist[0] = 0
    from collections import deque
    q = deque([0])
    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    if dist[-1] == -1:
        print(0)
        return
    ans = 1
    for i in range(1, N):
        cnt = 0
        for v in G[i]:
            if dist[v] == dist[i] - 1:
                cnt += 1
        ans = ans * cnt % MOD
    print(ans)

if __name__ == '__main__':
    main()