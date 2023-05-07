def main():
    # R行目、C列目のマスの色を出力する
    R, C = map(int, input().split())
    # グリッドの初期化
    grid = [['white' for i in range(15)] for j in range(15)]
    # グリッドの塗りつぶし
    for i in range(15):
        for j in range(15):
            if (i + j) % 2 == 0:
                grid[i][j] = 'black'
    # 結果の出力
    print(grid[R - 1][C - 1])

if __name__ == '__main__':
    main()