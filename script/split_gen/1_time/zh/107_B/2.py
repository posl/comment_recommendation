def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    # 从上往下找，找到第一个有黑色的行
    for i in range(H):
        if '#' in a[i]:
            first_black_row = i
            break
    # 从下往上找，找到第一个有黑色的行
    for i in range(H-1, -1, -1):
        if '#' in a[i]:
            last_black_row = i
            break
    # 从左往右找，找到第一个有黑色的列
    for i in range(W):
        if '#' in [a[j][i] for j in range(H)]:
            first_black_col = i
            break
    # 从右往左找，找到第一个有黑色的列
    for i in range(W-1, -1, -1):
        if '#' in [a[j][i] for j in range(H)]:
            last_black_col = i
            break
    # 输出结果
    for i in range(first_black_row, last_black_row+1):
        print(a[i][first_black_col:last_black_col+1])
