def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    def dfs(v, p=-1):
        d[v] = d[p] + 1
        for u in g[v]:
            if u == p:
                continue
            dfs(u, v)
    n, q = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    d = [0] * n
    dfs(0)
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (d[c] + d[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')
