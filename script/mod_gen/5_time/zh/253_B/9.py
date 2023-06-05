def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    # 2つのoの位置を探す
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                o1 = (i, j)
            if S[i][j] == "o":
                o2 = (i, j)
    # 4方向に移動する
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    # 探索済みの位置を記録する
    visited = [[False] * W for _ in range(H)]
    # 探索する
    def dfs(y, x, depth):
        if y < 0 or H <= y or x < 0 or W <= x:
            return float("inf")
        if S[y][x] == "-":
            return float("inf")
        if visited[y][x]:
            return float("inf")
        if (y, x) == o2:
            return depth
        visited[y][x] = True
        res = float("inf")
        for dy, dx in d:
            res = min(res, dfs(y + dy, x + dx, depth + 1))
        visited[y][x] = False
        return res
    ans = dfs(o1[0], o1[1], 0)
    print(ans - 1)

if __name__ == '__main__':
    main()