def main():
    from sys import stdin
    from collections import defaultdict
    def input(): return stdin.readline().strip()
    N, Q = map(int, input().split())
    edges = defaultdict(list)
    for i in range(N - 1):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    cnt = [0] * (N + 1)
    for i in range(Q):
        p, x = map(int, input().split())
        cnt[p] += x
    ans = [0] * (N + 1)
    def dfs(v, p):
        for u in edges[v]:
            if u == p: continue
            dfs(u, v)
            cnt[v] += cnt[u]
    dfs(1, -1)
    print(*cnt[1:])

if __name__ == '__main__':
    main()