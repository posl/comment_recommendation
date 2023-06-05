def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 各行各列的障碍物数
    row = [0] * H
    col = [0] * W
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                row[i] += 1
                col[j] += 1
    # 各行各列的障碍物数的最大值
    max_row = max(row)
    max_col = max(col)
    # 最大值的行数和列数
    row_num = row.count(max_row)
    col_num = col.count(max_col)
    # 最大值的行数和列数的交叉点
    # 交叉点上有障碍物则最大值减一
    cross = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#' and row[i] == max_row and col[j] == max_col:
                cross = 1
    print(max_row + max_col - cross)

if __name__ == '__main__':
    solve()