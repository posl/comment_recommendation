def main():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    c = [0] * M
    for i in range(M):
        a[i], b[i], c[i] = map(int, input().split())
    for i in range(M):
        a[i] -= 1
        b[i] -= 1
    #print(N, M, a, b, c)
    d = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for i in range(M):
        d[a[i]][b[i]] = c[i]
    #print(d)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    #print(d)
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if d[i][j] == d[i][k] + d[k][j]:
                    ans += d[i][j]
    print(ans)
