def solve():
    N, M = map(int, input().split())
    INF = 10 ** 9
    d = [[INF for i in range(N + 1)] for j in range(N + 1)]
    for i in range(M):
        a, b, c = map(int, input().split())
        d[a][b] = c
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if d[i][j] == d[i][k] + d[k][j]:
                    ans += d[i][j]
    print(ans)
solve()
