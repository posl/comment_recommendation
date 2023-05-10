def solve():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(N)]
    xyr.append([s_x, s_y, 0])
    xyr.append([t_x, t_y, 0])
    N += 2
    def check(i, j):
        xi, yi, ri = xyr[i]
        xj, yj, rj = xyr[j]
        d = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5
        return d <= ri + rj
    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if check(i, j):
                graph[i][j] = 1
                graph[j][i] = 1
    from collections import deque
    def bfs(s):
        INF = 10 ** 18
        dist = [INF] * N
        dist[s] = 0
        que = deque([s])
        while que:
            v = que.popleft()
            for nv in range(N):
                if graph[v][nv] and dist[nv] == INF:
                    dist[nv] = dist[v] + 1
                    que.append(nv)
        return dist
    dist = bfs(N - 2)
    if dist[N - 1] == INF:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    solve()