def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    circles.append([s_x, s_y, 0])
    circles.append([t_x, t_y, 0])
    N += 2
    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if d <= r1 + r2:
                graph[i][j] = 1
                graph[j][i] = 1
    seen = [False] * N
    def dfs(v):
        seen[v] = True
        for i in range(N):
            if graph[v][i] == 1 and seen[i] == False:
                dfs(i)
    dfs(N - 2)
    if seen[N - 1]:
        print('Yes')
    else:
        print('No')
