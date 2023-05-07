def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = ((XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2) ** 0.5
    def dfs(v, visited):
        if len(visited) == N:
            return 0
        res = 0
        for u in range(N):
            if u in visited:
                continue
            visited.add(u)
            res += dist[v][u] + dfs(u, visited)
            visited.remove(u)
        return res
    print(dfs(0, {0}) / math.factorial(N))

if __name__ == '__main__':
    main()