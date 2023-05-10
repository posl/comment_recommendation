def dfs(x,y):
    if x<0 or x>=1000 or y<0 or y>=1000:
        return
    if field[x][y] == 0:
        return
    field[x][y] = 0
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
n = int(input())
field = [[0]*1000 for _ in range(1000)]
for _ in range(n):
    x,y = map(int,input().split())
    field[x][y] = 1
ans = 0
for i in range(1000):
    for j in range(1000):
        if field[i][j] == 1:
            dfs(i,j)
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()