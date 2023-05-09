def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    ans = [0] * N
    def dfs(cur, par):
        for nxt, w in G[cur]:
            if nxt == par:
                continue
            if w % 2 == 0:
                ans[nxt] = ans[cur]
            else:
                ans[nxt] = 1 - ans[cur]
            dfs(nxt, cur)
    dfs(0, -1)
    print(*ans, sep = '
')

if __name__ == '__main__':
    main()