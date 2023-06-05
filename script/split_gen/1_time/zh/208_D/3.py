def floyd_warshall(d):
    for k in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
N, M = map(int, input().split())
d = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
floyd_warshall(d)
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            ans += d[i][j] if d[i][j] < float('inf') and d[i][j] == d[i][k]+d[k][j] else 0
print(ans)
