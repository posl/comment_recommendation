def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))
    # グリッドの縦横の最大値
    max_num = 1000
    # グリッドの縦横の最小値
    min_num = -1000
    # グリッドの縦横の最大値と最小値からグリッドの縦横の長さを求める
    h = max_num - min_num + 1
    w = max_num - min_num + 1
    # グリッドを作成する
    grid = [[0 for i in range(w)] for j in range(h)]
    # 黒いマスを塗る
    for i in range(N):
        x = xy[i][0] - min_num
        y = xy[i][1] - min_num
        grid[y][x] = 1
    # 黒いマスの数
    black = 0
    # 黒いマスがあるかどうかを確認する
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                black += 1
                break
    # 黒いマスがない場合は0を出力する
    if black == 0:
        print(0)
        return
    # 黒いマスがある場合は連結成分を調べる
    else:
        # 黒いマスの数
        black = 0
        # 白いマスを塗る
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    grid[i][j] = -1
        # 黒いマスの数
        black = 0
        # 黒いマスがあるかどうかを確認する
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    black +=
