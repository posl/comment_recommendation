def main():
    # 读入数据
    H, W = map(int, input().split())
    # 读入矩阵
    a = [input() for _ in range(H)]
    # 从上往下遍历
    for i in range(H):
        # 从左往右遍历
        for j in range(W):
            # 如果遇到黑色方块，则跳过
            if a[i][j] == "#":
                break
        # 如果遇到黑色方块，则跳过
        if a[i][j] == "#":
            continue
        # 如果该行只有白色方块，则删除该行
        else:
            del a[i]
            # 删除该行后，行数减一
            H -= 1
            # 因为删除了一行，所以要减一，以免跳过下一行
            i -= 1
    # 从左往右遍历
    for j in range(W):
        # 从上往下遍历
        for i in range(H):
            # 如果遇到黑色方块，则跳过
            if a[i][j] == "#":
                break
        # 如果遇到黑色方块，则跳过
        if a[i][j] == "#":
            continue
        # 如果该列只有白色方块，则删除该列
        else:
            # 从上往下删除该列
            for i in range(H):
                # 删除该列
                a[i] = a[i][:j] + a[i][j + 1:]
            # 删除该列后，列数减一
            W -= 1
            # 因为删除了一列，所以要减一，以免跳过下一列
            j -= 1
    # 输出最终状态
    for i in range(H):
        print(a[i])
