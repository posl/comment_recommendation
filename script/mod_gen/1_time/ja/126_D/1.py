def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    ans = [0] * N
    def dfs(u, p, c):
        ans[u] = c
        for v, w in G[u]:
            if v == p:
                continue
            dfs(v, u, c ^ (w % 2))
    dfs(0, -1, 0)
    print(*ans, sep='
')

if __name__ == '__main__':
    main()