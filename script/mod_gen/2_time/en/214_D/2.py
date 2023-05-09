def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    def dfs(v, p):
        for u, w in G[v]:
            if u == p:
                continue
            dfs(u, v)
            s[v] += s[u] + w * s[u]
    s = [0] * N
    dfs(0, -1)
    def dfs2(v, p):
        for u, w in G[v]:
            if u == p:
                continue
            s[u] = s[v] + (N - 2 * s[u] - 1) * w
            dfs2(u, v)
    dfs2(0, -1)
    print(sum(s))
main()

if __name__ == '__main__':
    main()