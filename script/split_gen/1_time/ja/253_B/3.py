def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                start = (i, j)
                break
    def dfs(i, j, d):
        if i < 0 or j < 0 or i >= h or j >= w or s[i][j] == "#":
            return 0
        if s[i][j] == "o":
            return d
        s[i] = s[i][:j] + "#" + s[i][j + 1:]
        return max(dfs(i + 1, j, d + 1), dfs(i - 1, j, d + 1), dfs(i, j + 1, d + 1), dfs(i, j - 1, d + 1))
    print(dfs(start[0], start[1], 0))
