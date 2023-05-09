def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 1. find the black squares
    black = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                black.append((i, j))
    # 2. make a graph
    graph = {}
    for i, j in black:
        graph[(i, j)] = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (i + di, j + dj) in black:
                graph[(i, j)].append((i + di, j + dj))
    # 3. find the number of sides
    visited = set()
    def dfs(i, j):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for di, dj in graph[(i, j)]:
            dfs(di, dj)
    dfs(black[0][0], black[0][1])
    if len(visited) == len(black):
        print(4)
    else:
        print(3)
