def main():
    import sys
    sys.setrecursionlimit(1000000)
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    visited = [[0] * W for _ in range(H)]
    def dfs(i, j, cnt):
        if i < 0 or i >= H or j < 0 or j >= W or S[i][j] == '#' or visited[i][j]:
            return 10**9
        if i == D_h and j == D_w:
            return cnt
        visited[i][j] = 1
        res = 10**9
        res = min(res, dfs(i - 1, j, cnt + 1))
        res = min(res, dfs(i + 1, j, cnt + 1))
        res = min(res, dfs(i, j - 1, cnt + 1))
        res = min(res, dfs(i, j + 1, cnt + 1))
        res = min(res, dfs(i - 2, j - 2, cnt + 1))
        res = min(res, dfs(i - 2, j - 1, cnt + 1))
        res = min(res, dfs(i - 2, j, cnt + 1))
        res = min(res, dfs(i - 2, j + 1, cnt + 1))
        res = min(res, dfs(i - 2, j + 2, cnt + 1))
        res = min(res, dfs(i - 1, j - 2, cnt + 1))
        res = min(res, dfs(i - 1, j + 2, cnt + 1))
        res = min(res, dfs(i, j - 2, cnt + 1))
        res = min(res, dfs(i, j + 2, cnt + 1))
        res = min(res, dfs(i + 1, j - 2, cnt + 1))
        res = min(res, dfs(i + 1, j + 2, cnt +
