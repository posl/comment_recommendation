def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #print(N)
    #print(X)
    #print(Y)
    #グリッドの生成
    grid = []
    for i in range(201):
        grid.append([0] * 201)
    #print(grid)
    #グリッドに塗りつぶし
    for i in range(N):
        grid[X[i]+100][Y[i]+100] = 1
    #print(grid)
    #連結成分の数を数える
    ans = 0
    for i in range(201):
        for j in range(201):
            if grid[i][j] == 1:
                ans += 1
                dfs(i, j, grid)
    print(ans)
