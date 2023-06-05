def dfs(x, y):
    global ans
    if x == h - 1 and y == w - 1:
        ans += 1
        return
    if x + 1 < h and s[x + 1][y] == '.':
        dfs(x + 1, y)
    if y + 1 < w and s[x][y + 1] == '.':
        dfs(x, y + 1)
    return
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
dfs(0, 0)
print(ans)

if __name__ == '__main__':
    dfs()