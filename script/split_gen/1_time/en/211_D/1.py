def main():
    import sys
    from collections import deque
    def input(): return sys.stdin.readline().strip()
    def list2d(a, b, c): return [[c] * b for i in range(a)]
    def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
    def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
    def ceil(x, y=1): return int(-(-x // y))
    def INT(): return int(input())
    def MAP(): return map(int, input().split())
    def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
    def Yes(): print('Yes')
    def No(): print('No')
    def YES(): print('YES')
    def NO(): print('NO')
    sys.setrecursionlimit(10 ** 9)
    INF = 10 ** 18
    MOD = 10 ** 9 + 7
    N, M = MAP()
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = MAP()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    # 1からの距離と1からの道の数
    dist = [-1] * N
    dist[0] = 0
    cnt = [0] * N
    cnt[0] = 1
    Q = deque([0])
    while Q:
        v = Q.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            cnt[nv] = cnt[v]
            Q.append(nv)
        for nv in G[v]:
            if dist[nv] == dist[v] + 1:
                cnt[nv] += cnt[v]
                cnt[nv] %= MOD
    print(cnt[-1])
