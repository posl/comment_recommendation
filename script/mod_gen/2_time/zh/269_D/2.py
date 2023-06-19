def dfs(x, y):
    if x < 0 or x >= 2001 or y < 0 or y >= 2001 or field[x][y] == 0:
        return
    field[x][y] = 0
    dfs(x-1, y-1)
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x+1, y)
    dfs(x+1, y+1)
    return
n = int(input())
field = [[0]*2001 for i in range(2001)]
for i in range(n):
    x, y = map(int, input().split())
    field[x+1000][y+1000] = 1
ans = 0
for i in range(2001):
    for j in range(2001):
        if field[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()