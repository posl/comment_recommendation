def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
N, M = map(int, input().split())
INF = 10**9
d = [[INF]*N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    d[A-1][B-1] = C
floyd_warshall()
ans = 0
for s in range(N):
    for t in range(N):
        for k in range(N):
            if d[s][t] == d[s][k] + d[k][t]:
                ans += d[s][t]
print(ans)

if __name__ == '__main__':
    floyd_warshall()