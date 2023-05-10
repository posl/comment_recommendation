def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
N, M = map(int, input().split())
d = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    d[A-1][B-1] = C
floyd_warshall()
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if d[i][j] != float('inf') and d[j][k] != float('inf') and d[k][i] != float('inf'):
                ans += d[i][j] + d[j][k] + d[k][i]
print(ans)

if __name__ == '__main__':
    floyd_warshall()