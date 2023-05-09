def main():
    # R:行 C:列
    R, C = map(int, input().split())
    # リストの初期化
    grid = []
    # リストに入力を追加
    for r in range(15):
        grid.append(list(input()))
    # リストの表示
    for r in range(15):
        print(grid[r])
    # リストの表示
    for r in range(15):
        print(grid[r][C-1], end="")
    print()
    # リストの表示
    for r in range(15):
        print(grid[R-1][r], end="")
    print()
    # 1行目とC列目の奇数偶数を調べる
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("white")
