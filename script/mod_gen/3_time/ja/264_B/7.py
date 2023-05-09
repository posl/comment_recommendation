def main():
    R, C = map(int, input().split())
    #黒白のグリッドを作成
    grid = [["black", "white"] * 8, ["white", "black"] * 8] * 8
    #黒白のグリッドのR行目C列目を出力
    print(grid[R-1][C-1])

if __name__ == '__main__':
    main()