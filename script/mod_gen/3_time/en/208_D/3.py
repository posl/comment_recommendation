def main():
    import sys
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
    MOD = 10**9 + 7
    N, M = MAP()
    G = list2d(N, N, INF)
    for i in range(N):
        G[i][i] = 0
    for i in range(M):
        a, b, c = MAP()
        a -= 1
        b -= 1
        G[a][b] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if G[i][j] == G[i][k] + G[k][j] and G[i][j] != INF:
                    ans += G[i][j]
    print(ans)

if __name__ == '__main__':
    main()