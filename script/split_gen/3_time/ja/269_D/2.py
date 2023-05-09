def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #座標の値が大きすぎるので、最大値を0にする
    X_max = max(X)
    Y_max = max(Y)
    X_min = min(X)
    Y_min = min(Y)
    X = [x - X_max for x in X]
    Y = [y - Y_max for y in Y]
    #グリッドの作成
    grid = [[0] * (2 * Y_max + 1) for i in range(2 * X_max + 1)]
    #グリッドに塗る
    for i in range(N):
        grid[X[i]][Y[i]] = 1
    #グリッドの表示
    for i in range(2 * X_max + 1):
        print(grid[i])
    #連結成分の数を数える
    count = 0
    for i in range(2 * X_max + 1):
        for j in range(2 * Y_max + 1):
            if grid[i][j] == 1:
                count += 1
                dfs(grid, i, j, X_max, Y_max)
    print(count)
