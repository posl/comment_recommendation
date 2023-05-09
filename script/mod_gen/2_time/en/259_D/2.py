def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x = [0] * N
    y = [0] * N
    r = [0] * N
    for i in range(N):
        x[i], y[i], r[i] = map(int, input().split())
    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
    for i in range(N):
        if (s_x - x[i]) ** 2 + (s_y - y[i]) ** 2 < r[i] ** 2:
            dist[i][N] = ((s_x - x[i]) ** 2 + (s_y - y[i]) ** 2) ** 0.5
        else:
            dist[i][N] = abs((s_x - x[i]) ** 2 + (s_y - y[i]) ** 2 - r[i] ** 2) ** 0.5
        if (t_x - x[i]) ** 2 + (t_y - y[i]) ** 2 < r[i] ** 2:
            dist[N][i] = ((t_x - x[i]) ** 2 + (t_y - y[i]) ** 2) ** 0.5
        else:
            dist[N][i] = abs((t_x - x[i]) ** 2 + (t_y - y[i]) ** 2 - r[i] ** 2) ** 0.5
    dist[N][N] = 0
    for k in range(N + 1):
        for i in range(N + 1):
            for j in range(N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    if dist[N][N] == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()