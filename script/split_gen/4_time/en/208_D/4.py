def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, M, *ABCL = map(int, read().split())
    INF = 10**15
    G = [[INF] * N for _ in range(N)]
    for a, b, c in zip(*[iter(ABCL)] * 3):
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
            if G[i][j] < INF:
                ans += G[i][j]
    print(ans)
