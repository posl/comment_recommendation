def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    N, M = map(int, input().split())
    d = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    dist = [-1] * (N + 1)
    dist[1] = 0
    mod = 10**9 + 7
    ans = [0] * (N + 1)
    ans[1] = 1
    def dfs(v):
        for nv in d[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                ans[nv] = ans[v]
                dfs(nv)
            elif dist[nv] == dist[v] + 1:
                ans[nv] += ans[v]
                ans[nv] %= mod
    dfs(1)
    print(ans[N])
