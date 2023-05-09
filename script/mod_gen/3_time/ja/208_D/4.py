def main():
    N, M = map(int, input().split())
    dist = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        dist[A - 1][B - 1] = C
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dist[i][j] == dist[i][k] + dist[k][j]:
                    ans += dist[i][k]
    print(ans)
main()

if __name__ == '__main__':
    main()