def main():
    n, m = map(int, input().split())
    a = [[False] * n for _ in range(n)]
    b = [[False] * n for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        a[x][y] = a[y][x] = True
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        b[x][y] = b[y][x] = True
    def dfs(x, y):
        if x == n: return True
        if y == n: return dfs(x + 1, x + 2)
        if a[x][y] != b[x][y]: return False
        return dfs(x, y + 1)
    print("Yes" if dfs(0, 1) else "No")

if __name__ == '__main__':
    main()