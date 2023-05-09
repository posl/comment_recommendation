def main():
    N = int(input())
    black = [tuple(map(int, input().split())) for _ in range(N)]
    black = set(black)
    visited = set()
    def dfs(i, j):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for di, dj in [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]:
            next_i = i + di
            next_j = j + dj
            if (next_i, next_j) in black:
                dfs(next_i, next_j)
    ans = 0
    for i, j in black:
        if (i, j) in visited:
            continue
        dfs(i, j)
        ans += 1
    print(ans)
